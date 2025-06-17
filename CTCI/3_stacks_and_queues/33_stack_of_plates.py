from CTCI.helpers.stacks import Stack

DEFAULT_STACK_MAX_SIZE = 10

class SetOfStacks:
    def __init__(self, max_stack_size = DEFAULT_STACK_MAX_SIZE) -> None:
        self.stacks = [Stack()]
        self.pointer = 0
        self.sizes = [0]
        self.max_size = max_stack_size

    def push(self, data):
        current_size = self.sizes[self.pointer]

        if current_size == self.max_size:
            self.pointer += 1
            self.stacks.append(Stack())
            self.sizes.append(0)

        current_stack = self.stacks[self.pointer]
        current_stack.push(data)
        self.sizes[self.pointer] += 1


    def pop(self):
        if self.pointer == 0 and self.sizes[0] == 0:
            raise Exception("Set of stacks is empty")
        current_size = self.sizes[self.pointer]
        if current_size == 0:
            self.pointer -= 1

        current_stack = self.stacks[self.pointer]
        data = current_stack.pop()
        self.sizes[self.pointer] -= 1

        return data

    def peek(self):
        if self.pointer == 0 and self.sizes[0] == 0:
            raise Exception("Set of stacks is empty")

        return self.stacks[self.pointer].peek()

    def is_empty(self):
        return self.pointer == 0 and self.sizes[0] == 0

    def pop_at(self, at):
        # TODO: fix this full nodes shift
        if at >= len(self.stacks):
            raise Exception("Invalid at value")

        temp_stack = Stack()
        data = self.stacks[at].pop()

        if at == len(self.stacks) - 1:
            return data


        for i in range(at + 1, len(self.stacks)):
            curr = self.stacks[i].pop()
            while curr:
                temp_stack.push(curr)
                curr = self.stacks[i].pop()

            from_temp = temp_stack.pop()
            while from_temp:
                self.push(from_temp)
                from_temp = temp_stack.pop()

        return data

def test_set_of_stacks():
    sos = SetOfStacks(max_stack_size=3)

    # Push 9 items, should create 3 internal stacks
    for i in range(9):
        sos.push(i)

    # Pop 3 items, should stay on the third stack
    assert sos.pop() == 8
    assert sos.pop() == 7
    assert sos.pop() == 6

    # Now should pop from second stack
    assert sos.pop() == 5
    assert sos.pop() == 4

    # Push more to refill the second stack
    sos.push(100)
    sos.push(101)

    # Check these are returned in LIFO order
    assert sos.pop() == 101
    assert sos.pop() == 100

    # Pop the rest
    assert sos.pop() == 3
    assert sos.pop() == 2
    assert sos.pop() == 1
    assert sos.pop() == 0

    # Edge case: popping when empty
    try:
        sos.pop()
        assert False, "Should raise or handle empty pop"
    except Exception:
        pass

    print("✅ All tests passed.")

def test_pop_at():
    sos = SetOfStacks(max_stack_size=3)

    # Push 10 elements (should create 4 stacks: [0-2], [3-5], [6-8], [9])
    for i in range(10):
        sos.push(i)

    # Test pop_at on middle stack (e.g., stack 1)
    val = sos.pop_at(1)
    assert val == 5  # LIFO for that sub-stack

    # Pop remaining items and ensure global LIFO is preserved
    results = []
    while not sos.is_empty():
        results.append(sos.pop())

    assert results == [9, 8, 7, 6, 4, 3, 2, 1, 0]  # 5 was removed earlier

    print("✅ pop_at tests passed.")

if __name__ == '__main__':
    test_set_of_stacks()
    test_pop_at()
