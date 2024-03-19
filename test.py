from cache import *

def test_cache_size():
    cache = ThisIsCache(2)
    cache.put(1)
    cache.put(2)
    assert len(cache.cache) == cache.size


def test_cache_size_not_exceeded():
    cache = ThisIsCache(2)
    cache.put(1)
    cache.put(2)
    cache.put(3)
    assert len(cache.cache) == cache.size


def test_cache_put_get():
    cache = ThisIsCache(3)
    cache.put(1)
    assert cache.get(1) == 1


def test_cache_get_invalid():
    cache = ThisIsCache(3)
    cache.put(1)
    assert cache.get(2) == -1


def test_cache_duplicate_put():
    cache = ThisIsCache(3)
    cache.put(1)
    assert cache.put(1) == -1


def test_cache_get_multiple_items():
    cache = ThisIsCache(3)
    cache.put(1)
    cache.put(2)
    cache.put(3)
    assert cache.get(1) == 1
    assert cache.get(2) == 2
    assert cache.get(3) == 3


def test_cache_get_removed_by_accessed():
    cache = ThisIsCache(2)
    cache.put(1)
    cache.put(2)
    cache.get(2)
    cache.get(1)
    cache.put(3)
    assert cache.get(2) == -1


def test_cache_get_removed_by_created():
    cache = ThisIsCache(2)
    cache.put(1)
    cache.put(2)
    cache.put(3)
    assert cache.get(1) == -1
