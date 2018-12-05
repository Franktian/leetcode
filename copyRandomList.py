# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        ht = {}

        first = second = head

        while first:
            ht[first] = RandomListNode(first.label)
            first = first.next

        while second:
            ht[second].next = ht.get(second.next)
            ht[second].random = ht.get(second.random)
            second = second.next

        return ht.get(head)
