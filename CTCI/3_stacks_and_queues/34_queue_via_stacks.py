from CTCI.helpers.stacks import Stack

# How would I optimize this:
# Normally when there are a lot of elements removal will be O(n), so I'd move everything to helper_stack as soon as I receive a read or remove operation (peek, remove, is_empty)
# and just move everything to the main queue when calling add operation

class MyQueue:
    def __init__(self) -> None:
        self.push_stack = Stack()
        self.helper_stack = Stack()

    def add(self, data):
        if self.helper_stack.is_empty():
            self.push_stack.push(data)
            return

        self._helper_to_push_stack()
        self.push_stack.push(data)

    def _helper_to_push_stack(self):
        from_helper = self.helper_stack.pop()
        while from_helper:
            self.push_stack.push(from_helper)
            from_helper = self.helper_stack.pop()

    def _push_to_helper_stack(self):
        curr = self.push_stack.pop()
        while curr:
            self.helper_stack.push(curr)
            curr = self.push_stack.pop()

    def remove(self):
        if self.push_stack.is_empty():
            return self.helper_stack.pop()

        self._push_to_helper_stack()
        data = self.helper_stack.pop() # Take the first
        self._helper_to_push_stack()

        return data

    def peek(self):
        if self.push_stack.is_empty():
            return self.helper_stack.top.data

        self._push_to_helper_stack()
        data = self.helper_stack.top.data

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
