
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

def print_list(node):
    while node is not None:
        print(node, end=" ")
        node = node.next
    print()

def print_backword(list):
    if list is None: return
    print_backword(list.next)
    print(list, end=" ")

def print_backword_nicely(list):
    print("[", end = " ")
    print_backword(list)
    print("]")


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4

print_list(node1)
print_backword_nicely(node1)
