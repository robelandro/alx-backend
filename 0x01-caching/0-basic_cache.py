#!/usr/bin/python3
""" BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache defines:
      - overwrite functions of BaseCaching
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        The function returns the value associated with a given key in a cache

        :param key: The key is a unique identifier used to retrieve
        :return: If the key is present in the cache_data dictionary
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
