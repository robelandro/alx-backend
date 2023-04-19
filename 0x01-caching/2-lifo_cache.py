#!/usr/bin/python3
""" LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache- class that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        init
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        put method
        """
        if key and item:
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)
            self.cache_data[key] = item
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                last = self.keys.pop(-2)
                del self.cache_data[last]
                print("DISCARD: {}".format(last))

    def get(self, key):
        """
        get method
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
