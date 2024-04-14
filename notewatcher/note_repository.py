import os
from comutils import CopyDirectory, RemoteRepository

class NoteRepository(RemoteRepository, CopyDirectory):
    def __init__(self, path):
        super().__init__(path)
        self._ensure_remote_origin()

    def _ensure_remote_origin(self):
        username = os.path.basename(self.path)
        if not self.remote_origin_exists():
            self.create_remote_origin(username, 'notewatcher-notes')

    def get_note_path(self, username, file_name):
        return self.join(username, file_name)
