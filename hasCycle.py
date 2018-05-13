def hasCycle(head):
    ht = {}

    while head:
        if not ht.get(head):
            ht[head] = 1
        else:
            return True
        head = head.next

    return False

def hasCycleTwoPointer(head):
    if head == None or head.next == None:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if fast == None or fast.next == None:
            return False
        slow = slow.next
        fast = fast.next.next

    return True
