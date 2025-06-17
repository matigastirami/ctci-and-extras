class StackNode:
    def __init__(self, data) -> None:
        super().__init__()
        self.data = data
        self.next = None

class Stack:
    def push(self, data):
        node = StackNode(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            return None
        node = self.top
        self.top = node.next
        return node.data

    def peek(self):
        if not self.top:
            return None
        return top.data

    def is_empty(self):
        return self.top is None
