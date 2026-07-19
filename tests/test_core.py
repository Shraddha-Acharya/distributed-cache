import sys
import os
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