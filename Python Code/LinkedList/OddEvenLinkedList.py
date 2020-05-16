class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.right = None

def odd_even(root):
    curr = root
    head1, head2 = root.next, root.next

    while head1.next is not None and head1.next.next is not None:
        curr.next = head1.next
        head1.next = head1.next.next
        curr = curr.next
        head1 = head1.next

    if head1.next is not None:
        curr.next = head1.next
        curr = curr.next
    curr.next = head2
    head1.next = None
    return root
