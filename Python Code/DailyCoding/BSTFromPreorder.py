'''
Return the root node of a binary search tree that matches the given preorder traversal.
Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]


'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BST:
    def bstfrompreorder(self, preorder):
        if not preorder:
            return None

        curr = preorder[0]
        left, right = [], []
        i, j = 0, 0

        while i < len(preorder):
            if preorder[i] < curr:
                break
            i += 1
        while j < len(preorder):
            if preorder[j] > curr:
                break
            j += 1
        left, right = preorder[i:j], preorder[j:]

        ans = TreeNode(curr)
        if left:
            ans.left = self.bstfrompreorder(left)
            ans.right = self.bstfrompreorder(right)
        return ans
