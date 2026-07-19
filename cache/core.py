import time
from threading import Lock


class Cache:
    """A simple thread-safe in-memory key-value cache."""

    def __init__(self):
        self._store = {}   # key -> value
        self._lock = Lock()

    def set(self, key, value):
        with self._lock:
            self._store[key] = value

    def get(self, key):
        with self._lock:
            return self._store.get(key)

    def delete(self, key):
        with self._lock:
            return self._store.pop(key, None) is not None

    def __len__(self):
        return len(self._store)