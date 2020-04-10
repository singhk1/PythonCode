class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class SinglyLinkedList:
    """
    Creation of single linkedlist takes O(1) -- constant time
    """
    def __init__(self):
        self.head = None

    def __str__(self):
        """
        String representation takes O(n) --linear time
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(str(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def append(self, data):
        """
            Insert an element at the end of the list -- O(n) linear time
        """
        if not self.head:
            self.head = ListNode(data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data)

    def reverse(self):
        curr = self.head
        prev, next = None, None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def reverse_between(self, m, n):
        dummy = ListNode(-1)
        pre = dummy
        dummy.next = self.head
        for i in range(m - 1):
            pre = pre.next
        curr = pre.next
        while(m < n):
            temp = curr.next
            curr.next = temp.next
            temp.next = pre.next
            pre.next = temp
            m += 1
        return dummy.next

    def plus_one(self):
        first = ListNode(0)
        first.next = self.head
        not_nine = first

        while self.head:
            if self.head.data != 9:
                not_nine = self.head
            self.head = self.head.next
        not_nine.data += 1
        not_nine = not_nine.next

        while not_nine:
            not_nine.data = 0
            not_nine = not_nine.next
        return first if first.data else first.next


lst = SinglyLinkedList()
#print(lst)
lst.append(9)
lst.append(9)
lst.append(9)
lst.append(9)
lst.append(0)
print(lst)
#lst.reverse_between(2, 4)
#print(lst)
#lst.reverse()
#print(lst)
lst.plus_one()
print(lst)
