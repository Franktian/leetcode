def rotateRight(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if not head:
        return None
    
    if not head.next:
        return head
    
    n = 0
    curr = head
    while curr:
        n += 1
        curr = curr.next
    
    k %= n
    
    if k == 0:
        return head
    
    slow = fast = head
    
    for _ in range(k):
        fast = fast.next
    
    while fast.next:
        slow = slow.next
        fast = fast.next
    
    tmp = slow.next
    slow.next = None
    fast.next = head
    
    return tmp