from comutils import CommandUser
from notewatcher.note_repository import NoteRepository


NOTES_DIRECTORY = 'notes'


class NotewatcherUser(CommandUser):
    def __init__(self):
        super().__init__('notewatcher')

    def note_repo_path(self, username):
        return self.join(NOTES_DIRECTORY, username)
    
    def get_personal_note_repo(self):
        personal_notes_repo_path = self.note_repo_path(self._get_personal_username())
        personal_notes_repo = NoteRepository(personal_notes_repo_path)
        return personal_notes_repo

    def _get_personal_username(self):
        if not self.config.has_config('username'):
            raise KeyError("Configure your github username with 'notewatcher configure --username <your-github-username>'")
        return self.config.get_config('username')
