class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None 
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}     # map from key to Node

        # dummy nodes for accessing edges of the linked list
        # left = least recently used
        # right = most recently used
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        
    # remove node from list
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    # insert node at right
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:

        if key in self.cache:
            # remove it from its current position
            self.remove(self.cache[key])
            # add it to the right of the list
            self.insert(self.cache[key])

            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # Remove LRU from the list
            lru = self.left.next
            self.remove(lru)
            # Remove LRU from the cache
            del self.cache[lru.key]










