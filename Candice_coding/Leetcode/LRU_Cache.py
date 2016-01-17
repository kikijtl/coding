# Design and implement a data structure for Least Recently Used (LRU) cache. 
# It should support the following operations: get and set.
#  
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. 
# When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

class ListNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.length = 0
        self.head = None
        self.tail = None
        self.db = {}

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.db:
            return -1
        node = self.db[key]
        value = node.val
        self._moveToTail(node)
        return value
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        node = ListNode(key, value)
        if self.length < self.capacity and key not in self.db:
            self._insertNode(node)
            self.db[key] = node
        elif key not in self.db:
            self._retention()
            self._insertNode(node)
            self.db[key] = node
        else:
            # Overwrite the original val
            self.db[key].val = value
            node = self.db[key]
            self._moveToTail(node)
    
    def _insertNode(self, node):
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            self._addTail(node)
        self.length += 1
    
    def _addTail(self, node):
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
    
    def _retention(self):
        k = self.head.key
        self.head = self.head.next
        if self.head:
            if self.tail == self.head:
                self.tail.prev = None
            self.head.prev = None
        else:
            self.tail = None
        self.db.pop(k)
        self.length -= 1
    
    def _moveToTail(self, node):
        if self.tail == node:
            return
        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.next = None
        node.prev = self.tail
        self.tail.next = node
        self.tail = node


if __name__ == '__main__':
    capacity = 2
    cache = LRUCache(capacity)
    print [cache.set(2,1), cache.set(1,1), cache.get(2), cache.set(4,1), cache.get(1), cache.get(2)]