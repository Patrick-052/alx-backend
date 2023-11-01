#!/usr/bin/env python3
""" LRU Caching """

from typing import Any
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU cache system """

    def __init__(self):
        """ Initialize class instance """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key: str, item: Any) -> None:
        """ Adding an item in cache by clearing out the least recently
            used item in the cache if it reaches the maximum capacity """
        if key and item:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)

            elif len(self.cache_data) >= self.MAX_ITEMS:
                popped = self.cache_data.popitem(last=False)
                print(f"DISCARD: {popped[0]}")
            self.cache_data[key] = item

    def get(self, key: str) -> Any:
        """ Retrieving an item from cache """
        if key and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
