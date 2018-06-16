class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashvalues = {}
        

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        hash_val = key % 100
        if hash_val not in self.hashvalues:
            self.hashvalues[hash_val] = [key]
        else:
            self.hashvalues[hash_val].append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        hash_val = key % 100
        if not self.contains(hash_val):
            return
        self.hashvalues[hash_val].remove(key)

        if len(self.hashvalues[hash_val]) == 0:
            self.hashvalues.pop(hash_val)


    def contains(self, key):
        """
        Returns true if this set did not already contain the specified element
        :type key: int
        :rtype: bool
        """
        hash_val = key % 100
        return hash_val in self.hashvalues and key in self.hashvalues[hash_val]