from notewatcher.notewatcher_user import NotewatcherUser
from notewatcher.note_repository import NoteRepository
from notewatcher.note_map import SerializableNoteMap
from comutils import RemoteRepositoryNotFoundError


NOTE_MAP_KEY = 'note_map'


class Notetaker(NotewatcherUser):
    def __init__(self):
        super().__init__()
        note_map_string = self.config.get_config(NOTE_MAP_KEY, SerializableNoteMap().serialize())
        self.note_map = SerializableNoteMap.deserialize(note_map_string)
        self.note_repos = {}
        for _, username in self.note_map.items():
            self._add_note_repo(username)

    def modify_note_map(self, map_modifying_function):
        map_modifying_function(self.note_map)
        self.config.set_config(NOTE_MAP_KEY, self.note_map.serialize())
        self.update()

    def _add_note_repo(self, username):
        try:
            self.note_repos[username] = NoteRepository(self.note_repo_path(username))
        except RemoteRepositoryNotFoundError:
            print(f"Could not add notes repo for {username}")

    def update(self):
        personal_username = self._get_personal_username()
        for file_path, username in self.note_map.items():
            if username in self.note_repos:
                self.note_repos[username].copy_file(file_path, personal_username)
        for notes_repo in self.note_repos.values():
            notes_repo.commit_and_push_active()


def reveal(file_path, username):
    Notetaker().modify_note_map(lambda m: m.add_pair(file_path, username))


def hide(file_path, username):
    Notetaker().modify_note_map(lambda m: m.remove_pair(file_path, username))


def update():
    Notetaker().update()
