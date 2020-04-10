import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
max = 0
def largestBSTUtil(root):
    size = 0
    lower = sys.maxsize
    upper = -sys.maxsize - 1
    isBST = False
    if root is None:
        isBST = True

    left = largestBSTUtil(root.left)
    right = largestBSTUtil(root.right)
    lower = min(root.data, min(left.lower, right.lower))
    upper = max(root.data, max(left.upper, right.upper))
    

def largestBSTSubTree(root):
    if root is None:
        return 0
    largestBSThealper(root)
    return max
