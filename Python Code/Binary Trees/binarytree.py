from queue import deque
class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, curr_node):
        if value < curr_node.value:
            if curr_node.left == None:
                curr_node.left = Node(value)
            else:
                self._insert(value, curr_node.left)
        elif value > curr_node.value:
            if curr_node.right == None:
                curr_node.right = Node(value)
            else:
                self._insert(value, curr_node.right)
        else:
            print('Value already in the tree')

    def print_tree_inorder(self):
        if self.root != None:
            self._print_tree_inorder(self.root)

    def _print_tree_inorder(self, curr_node):
        if curr_node != None:
            self._print_tree_inorder(curr_node.left)
            print(str(curr_node.value), end =" ")
            self._print_tree_inorder(curr_node.right)

    def print_tree_preorder(self):
        if self.root != None:
            self._print_tree_preorder(self.root)

    def _print_tree_preorder(self, curr_node):
        if curr_node != None:
            print(str(curr_node.value), end =" ")
            self._print_tree_preorder(curr_node.left)
            self._print_tree_preorder(curr_node.right)

    def print_tree_postorder(self):
        if self.root != None:
            self._print_tree_postorder(self.root)

    def _print_tree_postorder(self, curr_node):
        if curr_node != None:
            self._print_tree_postorder(curr_node.left)
            self._print_tree_postorder(curr_node.right)
            print(str(curr_node.value), end =" ")

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0
    def _height(self, curr_node, curr_height):
        if curr_node == None: return curr_height
        left_height = self._height(curr_node.left, curr_height + 1)
        right_height = self._height(curr_node.right, curr_height + 1)
        return max(left_height, right_height)

    def invert(self, root):
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                node.left, node.right = node.right, node.left
                q.append(node.left)
                q.append(node.right)
        return root

    def findTilt(self, root):
        res = [0]
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            res[0] += abs(left - right)
            return root.value + left + right
        helper(root)
        return res[0]
    def preorderTraversalIterative(self, root):
        res = []
        cur = root

        while cur:
            if not cur.left:
                res.append(cur.value)
                cur = cur.right
            else:
                predecessor = cur.left

                while predecessor.right and predecessor.right != cur:
                    predecessor = predecessor.right

                if not predecessor.right:
                    predecessor.right = cur
                    res.append(cur.value)
                    cur = cur.left
                else:
                    predecessor.right = None
                    cur = cur.right
        return res

tree = BinaryTree()
tree.insert(27)
tree.insert(14)
tree.insert(35)
tree.insert(10)
tree.insert(19)
tree.insert(31)
tree.insert(42)
print(tree.preorderTraversalIterative(Node(27)))
print("Inorder --> ", end =" ")
tree.print_tree_inorder()
print()
print("tree height --> " + str(tree.height()))
print("preorder --> ", end =" ")
tree.print_tree_preorder()
print()
print("Postorder -->", end=" ")
tree.print_tree_postorder()
tree.invert(Node(27))
print("Inorder after invertion--> ", end =" ")
tree.print_tree_inorder()
print("tilt ->")
print(tree.findTilt(Node(27)))
