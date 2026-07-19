import time
from threading import Lock


class Cache:
    """A simple thread-safe in-memory cache with optional TTL expiry."""

    def __init__(self):
        self._store = {}      # key -> value
        self._expiry = {}     # key -> expiry timestamp (float, epoch seconds)
        self._lock = Lock()

    def set(self, key, value, ttl=None):
        """
        Store a key-value pair.
        ttl: optional, time-to-live in seconds. If None, key never expires.
        """
        with self._lock:
            self._store[key] = value
            if ttl is not None:
                self._expiry[key] = time.time() + ttl
            else:
                self._expiry.pop(key, None)  # ensure no stale expiry remains

    def get(self, key):
        with self._lock:
            if self._is_expired(key):
                self._delete_unlocked(key)
                return None
            return self._store.get(key)

    def delete(self, key):
        with self._lock:
            return self._delete_unlocked(key)

    def _delete_unlocked(self, key):
        """Internal delete, assumes lock is already held."""
        existed = self._store.pop(key, None) is not None
        self._expiry.pop(key, None)
        return existed

    def _is_expired(self, key):
        """Internal check, assumes lock is already held."""
        expiry_time = self._expiry.get(key)
        if expiry_time is None:
            return False
        return time.time() >= expiry_time

    def __len__(self):
        return len(self._store)