class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if not self.head:
            self.head = Node(data)
            return
        curr = self.head
        while curr:
            curr = curr.next
        curr.next = Node(data)
    
