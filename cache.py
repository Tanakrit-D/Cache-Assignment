from datetime import datetime
import time


class ThisIsCache:
    def __init__(self, size: int):
        self.cache = {}
        self.size = size

    def get(self, value: int, update: bool = True):
        try:
            self.cache[value]
            if update:
                setattr(self.cache[value], "accessed", datetime.now())
            return value
        except KeyError:
            return -1

    def put(self, value: int):
        if self.get(value, False) == -1:
            self.enforce_size()
            time.sleep(0.01)
            self.cache.update({value: CacheItem(value)})
            return None
        else:
            return -1

    def enforce_size(self):
        if len(self.cache) == self.size:
            self.remove_by_access_datetime()

    def remove_by_access_datetime(self):
        try:
            list_by_access = sorted(
                self.cache.items(),
                key=lambda cache_item: getattr(cache_item[1], "accessed"),
            )
            self.cache.pop(list_by_access[0][0])
        except AttributeError:
            self.remove_by_creation_datetime()

    def remove_by_creation_datetime(self):
        list_by_created = sorted(
            self.cache.items(), key=lambda cache_item: getattr(cache_item[1], "created")
        )
        self.cache.pop(list_by_created[0][0])


class CacheItem:
    def __init__(self, value: int):
        self.value = value
        self.created = datetime.now()

    def __str__(self):
        created = datetime.strftime(self.created, "%Y/%m/%d %H:%M:%S")
        if hasattr(self, "accessed"):
            accessed = datetime.strftime(self.accessed, "%Y/%m/%d %H:%M:%S")
            return f"Value: {self.value}\nCreated: {created}\nAccessed: {accessed}"
        else:
            return f"Value: {self.value}\nCreated: {created}\nAccessed: Never"
