#!/usr/bin/env python3
""" LIFO Caching """

from typing import Any
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO cache system """

    def __init__(self):
        """ Initialize class instance """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key: str, item: Any) -> None:
        """ Adding an item in cache by clearing out the last item
            in the cache if it reaches the maximum capacity """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                popped = self.cache_data.popitem(last=True)
                print(f"DISCARD: {popped[0]}")
            self.cache_data[key] = item

    def get(self, key: str) -> Any:
        """ Retrieving an item from cache """
        return self.cache_data.get(key, None)
