"""
Design and implement an LRU (Least Recently Used) cache.
This is a cache with fixed size in terms of the number of items
it holds (supplied at instantiation).
The cache must allow client code to get items from the cache
and store items to the cache.
Once the cache is full, when the client wants to store a new item
in the cache, an old item must be overwritten or removed to
make room.
The item we will remove is the Least Recently Used (LRU) item.
"""

"""
double link list solution
"""

MAX_SIZE = 15


class LRUNode(object):
    def __init__(self, data, key):
        self._key = key
        self._data = data
        self._next = None
        self._prev = None

class LRUCache(object):
    def __init__(self, key=None, data=None):
        self._dict = {}
        self._size = 0
        self._head = None
        self._tail = None
        if data:
            self._head = LRUNode(data, key)
            self._dict[key] = self._head
            self._size = 1

    def get(self, key):
        my_node = self._dict.get(key, 0)
        if my_node:
            self.change_prio(my_node)
        else:
            self.set(key)

        return self._dict[key]._data

    def set(self, key):
        if self._dict.get(key):
            print "There is already a data there"
            # Update the data
        else:
            my_data = self.create_data(key)
            self._dict[key] = LRUNode(my_data, key)
            self.add_node(self._dict[key])

    def create_data(self, key):
        my_str = "{}_MY_TEST_DATA".format(key)
        return my_str

    def change_prio (self, node):
        if node != self._head:
            if node != self._tail:
                node._next._prev = node._prev
            node._prev._next, node._prev = node._next, None
            node._next, self._head._prev, self._head = self._head, node, node


    def add_node(self, node):
        if self._size == MAX_SIZE:
            self.remove_last_node()
        if self._head :
            node._next, self._head._prev, self._head = self._head, node, node
        else:
            self._head = node
        if not self._tail:
            self._tail = self._head._next
        self._size += 1

    def remove_last_node(self):
        if not self._head:
            print "Empty Cache"
            return
        if self._tail :
            self._dict.pop(self._tail._key)
            if self._tail._prev == self._head:
                self._head._next, self._tail = None, None
            else:
                self._tail, self._tail._prev._next = self._tail._prev, None
            self._size -= 1
        else:
            self._dict.pop(self._head._key)
            self._head, self._size = None, 0

