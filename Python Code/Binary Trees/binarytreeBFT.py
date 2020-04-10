from collections import defaultdict, deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def smallest_level(root):
    queue = deque([])
    queue.append((root, 0))

    level_to_sum = defaultdict(int)

    while queue:
        node, level = queue.popleft()
        level_to_sum[level] += node.val

        if node.right:
            queue.append((node.right, level + 1))
        if node.left:
            queue.append((node.left, level + 1))
    return min(level_to_sum, key = level_to_sum.get)
root = Node(5)
root.left = Node(2)
root.right = Node(5)

root.left.left = Node(1)
root.left.right = Node(3)

root.right.left = Node(1)
root.right.right = Node(7)

print(smallest_level(root))
