import sys
import os
import time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from cache.core import Cache


def test_set_and_get():
    c = Cache()
    c.set("a", 1)
    assert c.get("a") == 1


def test_get_missing_key_returns_none():
    c = Cache()
    assert c.get("nope") is None


def test_delete_existing_key():
    c = Cache()
    c.set("a", 1)
    assert c.delete("a") is True
    assert c.get("a") is None


def test_delete_missing_key_returns_false():
    c = Cache()
    assert c.delete("nope") is False


def test_overwrite_key():
    c = Cache()
    c.set("a", 1)
    c.set("a", 2)
    assert c.get("a") == 2


def test_len():
    c = Cache()
    c.set("a", 1)
    c.set("b", 2)
    assert len(c) == 2


def test_ttl_key_expires():
    c = Cache()
    c.set("a", 1, ttl=0.1)
    assert c.get("a") == 1
    time.sleep(0.15)
    assert c.get("a") is None


def test_ttl_none_means_no_expiry():
    c = Cache()
    c.set("a", 1)
    time.sleep(0.1)
    assert c.get("a") == 1


def test_ttl_overwritten_by_permanent_set():
    c = Cache()
    c.set("a", 1, ttl=0.1)
    c.set("a", 2)
    time.sleep(0.15)
    assert c.get("a") == 2


def test_expired_key_removed_from_store():
    c = Cache()
    c.set("a", 1, ttl=0.1)
    time.sleep(0.15)
    c.get("a")
    assert len(c) == 0


def test_delete_removes_expiry_entry():
    c = Cache()
    c.set("a", 1, ttl=10)
    c.delete("a")
    c.set("a", 2)
    time.sleep(0.05)
    assert c.get("a") == 2