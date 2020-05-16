class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def morris(root):
    curr = root

    while curr is not None:
        if curr.left is None:
            print(curr.data, end = " ")
            curr = curr.right
        else:
            # find the previous of curr
            prev = curr.left
            while prev.right is not None and prev.right != curr:
                prev = prev.right

            #make curr as right child of its previous
            if prev.right is None:
                prev.right = curr
                curr = curr.left
            else:
                prev.right = None
                print(curr.data, end= " ")
                curr = curr.right

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

morris(root)
