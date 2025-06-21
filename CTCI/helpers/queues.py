class QueueNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.first = None
        self.last = None

    def __str__(self) -> str:
        resp = ''
        iterator = self.first
        while iterator:
            resp += f'{iterator.data} -> '
            iterator = iterator.next
        resp += 'None'
        return resp

    def push(self, data):
        new_node = QueueNode(data)
        if self.last is not None:
            self.last.next = new_node

        self.last = new_node

        if self.first is None:
            self.first = self.last


    def pop(self):
        if self.first is None:
            return None

        data = self.first.data

        self.first = self.first.next

        if self.first is None:
            self.last = None

        return data

    def peek(self):
        if self.first is None:
            return None

        return self.first.data

    def is_empty(self):
        return self.first is None
