'''
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def flatten(root):
    if root is not None:
        flatten(root.left)
        flatten(root.right)

        if root.left:
            curr = root.left
            while curr.right:
                curr = curr.right
            curr.right = root.right
            root.right = root.left
            root.left = None
    return root


def pre_order(root):
    if root is None:
        return
    print(root.val, end='->')
    pre_order(root.left)
    pre_order(root.right)


root = TreeNode("1")
root.left = TreeNode("2")
root.right = TreeNode("5")
root.left.left = TreeNode("3")
root.left.right = TreeNode("4")
root.right.right = TreeNode("6")
flatten(root)
print(pre_order(root))
