# Cache Demo

## Overview
The main class, `ThisIsCache`, allows users to store and retrieve values within a dictionary-based cache.

Values are stored as `CacheItem` objects, containing the value itself along with metadata such as creation and last accessed timestamps.

### Features
- Stores values within a dictionary-based cache.
- Enforces a cache size.
- Uses `CacheItem` objects for storing values along with metadata.
- Allows storing items with `.put()` and retrieving them with `.get()`.
- Replaces existing items by sorting access datetime, and falls back to creation datetime.

## Running Demo
```
python demo.py
```

## Running Tests
```
pip install pytest
pytest test.py
```
