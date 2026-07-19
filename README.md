# distributed-cache

A Redis-like in-memory cache system built from scratch in Python — single-node core, network service, sharding, and replication.

## Features implemented

### Core cache
- Thread-safe `get` / `set` / `delete` operations, backed by a Python dict and a lock.

### TTL expiry
- Optional per-key time-to-live via `set(key, value, ttl=seconds)`.
- Lazy expiry: expired keys are detected and cleaned up on access, no background thread.

### LRU eviction
- Optional `max_size` cache limit.
- Least-recently-used keys are evicted first, tracked via an `OrderedDict`.
- Both reads (`get`) and writes (`set`) count as "use," refreshing recency.

## Run tests

```bash
pytest tests/ -v
```

## Roadmap
- [ ] Wrap cache in a TCP/HTTP server
- [ ] Benchmarking script for ops/sec
- [ ] Consistent hashing across multiple simulated nodes
- [ ] Leader-follower replication with failure simulation
- [ ] Load-testing script for real throughput/latency numbers
