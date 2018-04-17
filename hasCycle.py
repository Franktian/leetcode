def hasCycle(head):
    ht = {}

    while head:
        if not ht.get(head):
            ht[head] = 1
        else:
            return True
        head = head.next

    return False
