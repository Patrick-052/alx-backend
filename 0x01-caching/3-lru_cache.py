#!/usr/bin/env python3
""" LRU Caching """

from typing import Any
from time import time
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
            if len(self.cache_data) >= self.MAX_ITEMS:
                popped = self.cache_data.popitem(last=False)
                print(f"DISCARD: {popped[0]}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

    def get(self, key: str) -> Any:
        """ Retrieving an item from cache """
        return self.cache_data.get(key, None)
