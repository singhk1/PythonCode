class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#def mergeTwoLinkedLists

def mergeTwoLists(l1, l2):
    print(sorted(l1 + l2))

l1 = [1,3,5,7]
l2 = [-1, 0, 4, 8]

mergeTwoLists(l1, l2)
