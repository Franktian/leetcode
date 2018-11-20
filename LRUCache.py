class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.ht = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.ht.get(key):
            node = self.ht[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.ht.get(key):
            self._remove(self.ht.get(key))

        node = Node(key, value)
        self.ht[key] = node
        self._add(node)

        if len(self.ht) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.ht[node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)