
import json
import os

class SimpleKVDb(object):
    def __init__(self, filename=''):
        self.filename = filename
        if os.path.exists(filename) and os.path.getsize(filename) > 0 :
            self._load(self.filename)
        else:
            self.db = {}

    def _load(self, filename):
        with open(filename, 'r') as f:
            self.db = json.load(f)
            f.close()

    def set(self, k, v):
        self.db[k] = v

    def get(self, k):
        return self.db[k] if k in self.db.keys() else None

    def delete(self, k):
        if k in self.db.keys():
            self.db.pop(k)
            return True
        else:
            return False

    def flush(self):
        with open(self.filename, 'w') as f:
            json.dump(self.db, f)
            f.close()

    def get_all(self):
        return json.dumps(self.db)