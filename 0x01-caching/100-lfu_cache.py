#!/usr/bin/env python3
"""
LFUCache module
"""
from collections import defaultdict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache Latest Frequency Used caching system
    """

    def __init__(self) -> None:
        """Constructor
        """
        super().__init__()
        self.keys = []
        self.frequency = defaultdict(lambda: 0)

    def put(self, key, item):
        """Saves the item to the cache with the given key

        :param key: key to save the item
        :param item: item to save
        """
        if key is None or item is None:
            return

        if len(self.keys) == self.MAX_ITEMS and key not in self.keys:
            min_freq_key = min(self.frequency, key=self.frequency.get)
            self.keys.remove(min_freq_key)
            self.frequency.pop(min_freq_key)
            self.cache_data.pop(min_freq_key)
            print(f'DISCARD: {min_freq_key}')

        if key in self.keys:
            self.frequency[key] += 1
        else:
            self.keys.append(key)
            self.frequency[key] = 1

        self.cache_data[key] = item

    def get(self, key):
        """ Returns the value in self.cache_data linked to key

        :param key: key to search for
        """
        value = self.cache_data.get(key)
        if value is not None:
            self.frequency[key] += 1
            self.keys.remove(key)
            self.keys.append(key)
        return value
