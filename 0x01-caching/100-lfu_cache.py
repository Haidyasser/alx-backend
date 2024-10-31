#!/usr/bin/python3
""" LFU caching """
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU caching system that inherits from BasicCache"""

    def __init__(self):
        """ Initiliaze """
        super().__init__()
        self.dict = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.dict[key] += 1
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = min(self.dict, key=self.dict.get)
                del self.cache_data[discard]
                del self.dict[discard]
                print("DISCARD: {}".format(discard))
            self.cache_data[key] = item
            self.dict[key] = 1

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.dict[key] += 1
        return self.cache_data.get(key, None)
