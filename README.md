# distributed-cache

A Redis-like in-memory cache system built from scratch in Python, in stages:
single-node core → network service → sharding → replication.

## Day 1
- Thread-safe `get`/`set`/`delete` operations backed by a Python dict and a `threading.Lock`.
- Unit tests covering basic operations, overwrites, and missing-key behavior.

## Run tests
```bash
pytest tests/ -v
```

## Day 2
- Added optional TTL (time-to-live) expiry to `set()`.
- Lazy expiry: expired keys are detected and removed on `get()`, not via a background thread.
- Tests covering expiry, no-TTL permanence, TTL cleared on overwrite, and expiry cleanup on delete.