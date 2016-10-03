"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
"""

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.least = []
        

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.cache.keys():
            self.least.remove(key)
            self.least.append(key)
            return self.cache.get(key)
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.cache.keys():
            self.cache[key] = value
            self.least.remove(key)
            self.least.append(key)
        else:
            self.least.append(key)
            self.cache[key] = value

        if len(self.cache) > self.capacity:
            lru = self.least.pop(0)
            del self.cache[lru]


lru = LRUCache(1)
lru.set(2,1)
print lru.cache
print lru.get(2)

