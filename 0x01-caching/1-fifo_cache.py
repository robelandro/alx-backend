#!/usr/bin/python3
""" FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache- frist in frist out
    """
    def __init__(self):
        """ The constructor of the class
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ The function adds an item in the cache

        :param key: The key is a unique identifier used to retrieve
        :param item: The item is the value associated with the key
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                first = self.keys.pop(0)
                del self.cache_data[first]
                print("DISCARD: {}".format(first))

    def get(self, key):
        """
        The function returns the value associated with a given key in a cache

        :param key: The key is a unique identifier used to retrieve
        :return: If the key is present in the cache_data dictionary
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
