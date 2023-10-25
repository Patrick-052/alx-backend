#!/usr/bin/env python3
"""" Basic dictionary """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Implementing simple caching system"""

    def put(self, key, item):
        """ Adding an item in the cache """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieving an item from cache """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
