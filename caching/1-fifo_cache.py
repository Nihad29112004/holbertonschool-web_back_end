#!/usr/bin/python3
""" FIFO caching: Create a class FIFOCache that inherits from BaseCaching
                  and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ A FIFO Cache system. """

    def __init__(self):
        """ Initialize the cache. """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item to the cache (FIFO algorithm). """
        if key is None or item is None:
            return

        # If key already exists, update value but keep order
        if key in self.cache_data:
            self.cache_data[key] = item
            return

        # If cache is full, remove the first inserted key
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.keys.pop(0)
            del self.cache_data[discard]
            print(f"DISCARD: {discard}")

        # Add the new key/value
        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """ Get an item by key. """
        return self.cache_data.get(key, None)
