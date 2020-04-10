
#class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def maxLevelSum(self, root: TreeNode) -> int:
        mylist = [root]
        res = []
        while mylist:
            mylist2 = []
            sum = 0
            for node in mylist:
                if node.left:
                    mylist2.append(node.left)
                if node.right:
                    mylist2.append(node.right)
                sum += node.val
            res.append(sum)
            mylist = mylist2
        return res.index(max(res)) + 1
