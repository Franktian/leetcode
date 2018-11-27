class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ht = {}
        self.lst = []


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if not val in self.ht:
            self.ht[val] = len(self.lst)
            self.lst.append(val)
            return True
        return False


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.ht:
            idx = self.ht[val]
            last = self.lst[-1]

            # Copy over
            self.ht[last] = idx
            self.lst[idx] = last

            # Remove
            del self.ht[val]
            self.lst.pop()
            return True
        return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        from random import randint
        rand = randint(0, len(self.lst) - 1)
        return self.lst[rand]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()