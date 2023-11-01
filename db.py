
import json
import os
import logging

class SimpleKVDb(object):
    def __init__(self, filename=''):
        self.filename = filename
        self.setsCount = 0
        logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")
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
        self.setsCount += 1
        logging.info(f'setsCount has been increased. Current value is {self.setsCount}')
        if self.setsCount >= 5:
            self.flush()
            self.setsCount = 0

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
            logging.debug(f'The database has been flushed.')
            f.close()

    def get_all(self):
        return json.dumps(self.db)