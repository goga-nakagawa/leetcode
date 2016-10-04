"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
"""
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node): # O(1)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def delete(self, node): # O(1)
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        del node


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {} # { key: Node }
        self.least = LinkedList()

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.cache.keys():
            self.least.delete(self.cache[key])
            self.least.insert(Node(key, self.cache.get(key).value))
            return self.cache.get(key).value
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.cache.keys():
            self.least.delete(self.cache[key])
        elif len(self.cache) == self.capacity:
            del self.cache[self.least.head.key]
            self.least.delete(self.least.head)
        self.cache[key] = Node(key, value)
        self.least.delete(self.cache[key])
        self.least.insert(Node(key, value))


lru = LRUCache(1)
lru.set(2,1)
print lru.cache
print lru.get(2)

