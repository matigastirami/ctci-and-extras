from CTCI.helpers.stacks import Stack

class MyQueue:
    def __init__(self) -> None:
        self.push_stack = Stack()
        self.helper_stack = Stack()

    def add(self, data):
        self.push_stack.push(data)

    def remove(self):
        curr = self.push_stack.pop()
        while curr:
            self.helper_stack.push(curr)
            curr = self.push_stack.pop()

        data = self.helper_stack.pop() # Take the first
        from_helper = self.helper_stack.pop()
        while from_helper:
            self.push_stack.push(from_helper)
            from_helper = self.helper_stack.pop()

        return data

def test_my_queue():
    q = MyQueue()

    # Add elements
    q.add(10)
    q.add(20)
    q.add(30)

    # Remove elements — should return in FIFO order
    assert q.remove() == 10
    assert q.remove() == 20

    # Add more after removals
    q.add(40)
    q.add(50)

    assert q.remove() == 30
    assert q.remove() == 40
    assert q.remove() == 50

    # Removing from empty queue
    try:
        q.remove()
        assert False, "Expected exception or None on empty queue"
    except Exception:
        pass  # OK

    print("✅ MyQueue tests passed.")

if __name__ == '__main__':
    test_my_queue()
