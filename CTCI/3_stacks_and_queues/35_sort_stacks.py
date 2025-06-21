from CTCI.helpers.stacks import Stack


class SortedStack:
    def __init__(self) -> None:
        self.sorted = Stack()

    def __str__(self) -> str:
        return self.sorted.__str__()

    def push(self, data):
        helper_stack = Stack()
        while not self.sorted.is_empty() and self.sorted.peek() < data:
            helper_stack.push(self.sorted.pop())
        self.sorted.push(data)
        from_helper = helper_stack.pop()
        while from_helper:
            self.sorted.push(from_helper)
            from_helper = helper_stack.pop()

    def pop(self):
        return self.sorted.pop()

    def peek(self):
        return self.sorted.peek()

    def is_empty(self):
        return self.sorted.is_empty()

def test_sorted_stack():
    stack = SortedStack()

    # Push unsorted values
    stack.push(3)
    stack.push(1)
    stack.push(4)
    stack.push(2)
    stack.push(5)

    # Check peek is smallest
    assert stack.peek() == 1

    result = []
    while not stack.is_empty():
        result.append(stack.pop())

    assert result == [1, 2, 3, 4, 5]

    # Push again with descending order
    for v in [5, 4, 3, 2, 1]:
        stack.push(v)

    result = []
    while not stack.is_empty():
        result.append(stack.pop())

    assert result == [1, 2, 3, 4, 5]

    # Push same values multiple times
    for _ in range(3):
        stack.push(7)
    stack.push(5)
    stack.push(6)

    result = []
    while not stack.is_empty():
        result.append(stack.pop())

    assert result == [5, 6, 7, 7, 7]

    print("✅ All tests passed for SortedStack.")

if __name__ == "__main__":
    test_sorted_stack()
