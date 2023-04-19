#!/usr/bin/python3
""" LFUCache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache- Last Freq Used Cache
    """

    def __init__(self):
        """
        init
        """
        super().__init__()
        self.keys = {}

    def put(self, key, item):
        """
        put method
        """
        if key and item:
            if key in self.keys:
                self.keys[key] += 1
            else:
                self.keys[key] = 1
            self.cache_data[key] = item
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                min_key = min(self.keys, key=self.keys.get)
                del self.cache_data[min_key]
                del self.keys[min_key]
                print("DISCARD: {}".format(min_key))

    def get(self, key):
        """
        get method
        """
        if key in self.cache_data:
            self.keys[key] += 1
            return self.cache_data[key]
        return None
