def plusOne(head):
    st = []
    carry = 1
    while head:
        st.append(head)
        head = head.next

    while st != []:
        head = st.pop()
        r = head.val + carry

        carry = r / 10
        v = r % 10
        head.val = v

    if carry == 1:
        prev = ListNode(1)
        prev.next = head
        return prev

    return head
