class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
def getIntersectionNode(headA, headB):
    ht = {}

    while headA:
        if not ht.get(headA):
            ht[headA] = 1
        headA = headA.next

    while headB:
        if ht.get(headB):
            return headB
        headB = headB.next

    return None


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)

    a.next = b
    b.next = c
    d.next = e
    e.next = a

    f = getIntersectionNode(a, d)
    
    print f.val
