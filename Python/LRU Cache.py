class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.pev = None

class LRUCache(object):
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.right = Node(0,0)
        self.left = Node(0,0)
        self.left.next = self.right
        self.right.pev = self.left
    def insert(self,node):
        pevv = self.right.pev
        nextt = self.right
        print(pevv.val)
        pevv.next = node
        nextt.pev = node
        node.pev = pevv
        node.next = nextt
        print(node.pev.val)
    def delete(self, node):
        nextt = node.next
        pevv = node.pev
        nextt.pev = pevv
        pevv.next = nextt
    def get(self, key):
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, value):
        print("d")
        if key in self.cache:
            self.delete(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.delete(lru)
            del self.cache[lru.key]

        