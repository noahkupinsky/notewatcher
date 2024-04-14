from comutils import GithubAdapter
from notewatcher.notewatcher_user import NotewatcherUser
from notewatcher.file_viewer import FileViewer


class Watcher(NotewatcherUser):
    def __init__(self):
        super().__init__()

    def get_notewatcher_notes(self, personal_access_token):
        return GithubAdapter(personal_access_token).get_repo('notewatcher-notes')
    
    def view_file(self, file_path):
        if not self.config.has_config('viewdir'):
            raise KeyError("Configure your viewdir with 'notewatcher configure --viewdir <path-to-viewdir>'")
        viewdir = self.config.get_config('viewdir')
        file_viewer = FileViewer(viewdir)
        file_viewer.view_file(file_path)


def view(username, file_name):
    watcher = Watcher()
    note_repo = watcher.get_personal_note_repo()
    note_repo.pull(note_repo.active())
    note_path = note_repo.get_note_path(username, file_name)
    watcher.view_file(note_path)


def whitelist(notetaker_username, personal_access_token):
    notes = Watcher().get_notewatcher_notes(personal_access_token)
    notes.add_collaborator(notetaker_username, "push")


def blacklist(notetaker_username, personal_access_token):
    notes = Watcher().get_notewatcher_notes(personal_access_token)
    notes.remove_collaborator(notetaker_username)


