#!/usr/bin/python3
""" MRU Caching: Create a class MRUCache that inherits from BaseCaching
                 and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRU (Most Recently Used) Cache system. """

    def __init__(self):
        """ Initialize the cache. """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add key/value pair to cache data.
        If cache is full, discard the most recently used entry (MRU rule).
        """
        if key is None or item is None:
            return

        # If key already exists, update its value and mark as recently used
        if key in self.cache_data:
            self.cache_data[key] = item
            self.keys.remove(key)
            self.keys.append(key)
            return

        # If cache is full, remove the most recently used (last in list)
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.keys.pop(-1)
            del self.cache_data[discard]
            print(f"DISCARD: {discard}")

        # Add new item
        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """ Return the value stored in key.
        If key exists, mark it as recently used.
        """
        if key is None or key not in self.cache_data:
            return None

        # Mark as recently used
        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]

