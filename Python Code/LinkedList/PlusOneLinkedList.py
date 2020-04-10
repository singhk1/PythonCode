class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.iterator = None

    def iter_on(self):
        yield self
        if self.next:
            yield from self.next.iter_on()

    def __iter__(self):
        self.iterator = self.iter_on()
        return self

    def __next__(self):
        return next(self.iterator)

    def __str__(self):
        return "[%d]" % self.value

    def __repr__(self):
        return self.__str__()

    def print_on(self):
        print(*self.iter_on(), sep="->")


def make_list(number):
    root = None
    cur_node = None
    for digit_str in str(number):
        new_node = Node(int(digit_str))
        if cur_node:
            cur_node.next = new_node
        cur_node = new_node

        if not root:
            root = cur_node

    return root


def add_one(root):
    left_most_changeable = -1
    right_most_changeable = -1
    for idx, node in enumerate(root):
        if node.value < 9:
            left_most_changeable = idx
        right_most_changeable = idx

    for idx, node in enumerate(root):
        if left_most_changeable <= idx <= right_most_changeable:
            node.value += 1
            if node.value > 9:
                node.value = 0

    if left_most_changeable == -1:
        new_root = Node(1)
        new_root.next = root
        root = new_root

    return root


l = make_list(999)
l.print_on()  # [9]->[9]->[9]->[9]
l = add_one(l)
l.print_on()  # [1]->[0]->[0]->[0]->[0]
