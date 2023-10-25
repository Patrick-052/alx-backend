#!/usr/bin/env python3
"""" Basic dictionary """

from typing import Any
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Implementing simple caching system"""

    def put(self, key: str, item: Any) -> None:
        """ Adding an item in the cache """
        if key and item:
            self.cache_data[key] = item

    def get(self, key: str) -> Any:
        """ Retrieving an item from cache """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
