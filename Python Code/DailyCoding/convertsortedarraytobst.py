class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def converttoBST(ls):
    if not ls:
        return None

    mid = len(ls) // 2
    root = Node(ls[mid])
    root.left = converttoBST(ls[:mid])
    root.right = converttoBST(ls[mid + 1 :])

    return root


ls = [1, 2, 3, 4, 5, 6, 7]
converttoBST(ls)
