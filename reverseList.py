class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
def reverseList(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev

if __name__ == '__main__':
    a = ListNode(9)
    #b = ListNode(9)
    #c = ListNode(9)
    #a.next = b
    #b.next = c

    f = plusOne(a)
    
    while f:
        print f.val
        f = f.next
