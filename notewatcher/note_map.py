import os
import json
from comutils import Serializable


class PathUserPair(Serializable):
    def __init__(self, file_path, username):
        self.file_path = file_path
        self.username = username
        self._validate_file_path()

    def _validate_file_path(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")
        
    def __eq__(self, other):
        return self.file_path == other.file_path and self.username == other.username
    
    def serialize(self):
        return json.dumps({'file_path': self.file_path, 'username': self.username})
    
    @staticmethod
    def deserialize(string):
        return PathUserPair(*json.loads(string).values())


class AbstractNoteMap:
    def add_pair(self, file_path, username):
        pass
    
    def remove_pair(self, file_path, username):
        pass

    def items(self):
        pass


class SerializableNoteMap(Serializable, AbstractNoteMap):
    def __init__(self, pairs=[]):
        self.pairs = pairs

    def add_pair(self, file_path, username):
        pair = PathUserPair(file_path, username)
        if not pair in self.pairs:
            self.pairs.append(pair)
        
    def remove_pair(self, file_path, username):
        try:
            pair = PathUserPair(file_path, username)
            self.pairs.remove(pair)
        except ValueError:
            pass

    def items(self):
        return [(pair.file_path, pair.username) for pair in self.pairs]
    
    def serialize(self):
        return json.dumps([pair.serialize() for pair in self.pairs])
    
    @staticmethod
    def deserialize(string):
        return SerializableNoteMap([PathUserPair.deserialize(pair) for pair in json.loads(string)])
