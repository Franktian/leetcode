class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    head = ListNode(0)
    curr = head
    carry = 0

    while l1 or l2:
        if l1:
            v1 = l1.val
        else:
            v1 = 0
        
        if l2:
            v2 = l2.val
        else:
            v2 = 0
        
        s = v1 + v2 + carry
        carry = s / 10
        curr.next = ListNode(s % 10)

        curr = curr.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    if carry > 0:
        curr.next = ListNode(1)

    return head.next
