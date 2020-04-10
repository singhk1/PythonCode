# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        res = [0]
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            res[0] += abs(left - right)
            return root.val + left + right
        helper(root)
        return res[0]
