class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    sd = []
    curr = head

    while curr:
        sd.append(curr.val)
        curr = curr.next

    while len(sd) != 0:
        if sd.pop() != head.val:
            return False
        head = head.next

    return True

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(1)
    d = ListNode(2)
    e = ListNode(1)
    
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    
    print isPalindrome(a)
