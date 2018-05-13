class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeKLists(lists):
    
    vals = []
    for l in lists:
        head = l
        while head:
            vals.append(head.val)
            head = head.next
    
    vals.sort()

    head = ListNode(-1)
    curr = head

    for v in vals:
        node = ListNode(v)
        curr.next = node
        curr = node

    return head.next
