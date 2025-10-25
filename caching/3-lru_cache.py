#!/usr/bin/python3
""" LIFO Caching: Create a class LIFOCache that inherits from BaseCaching
                  and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ A LIFO Cache.
        Inherits from BaseCaching and discards the most recently added
        item when the cache reaches MAX_ITEMS.
    """

    def __init__(self):
        """ Initialize class instance. """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add key/value pair to cache data.
        If cache is full, discard the most recently added item (LIFO rule).
        """
        if key is None or item is None:
            return

        # If key already exists, update it and move to end
        if key in self.cache_data:
            self.cache_data[key] = item
            self.keys.remove(key)
            self.keys.append(key)
            return

        # If cache full, remove the last added key (LIFO)
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.keys.pop(-1)
            del self.cache_data[discard]
            print(f"DISCARD: {discard}")

        # Add new key
        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """ Return value stored in `key` of cache.
        If key is None or does not exist, return None.
        """
        return self.cache_data.get(key, None)

