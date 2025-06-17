class ArrayStacks:
    STACK_SIZE = 10
    TOTAL_STACKS = 3

    def __init__(self) -> None:
        self.stacks = [None] * (self.TOTAL_STACKS * self.STACK_SIZE)
        self.pointer_mapping = {
            "1": -1,
            "2": self.STACK_SIZE - 1,
            "3": (2 * self.STACK_SIZE) - 1
        }

    def _stack_base(self, stack: str) -> int:
        if stack == "1":
            return 0
        elif stack == "2":
            return self.STACK_SIZE
        elif stack == "3":
            return 2 * self.STACK_SIZE
        else:
            raise Exception("Invalid stack id")

    def push(self, data, stack: str):
        base = self._stack_base(stack)
        pointer = self.pointer_mapping[stack]

        if pointer + 1 >= base + self.STACK_SIZE:
            raise Exception(f"Stack {stack} is full capacity")

        self.pointer_mapping[stack] += 1
        self.stacks[self.pointer_mapping[stack]] = data


    def pop(self, stack: str):
        base = self._stack_base(stack)
        pointer = self.pointer_mapping[stack]

        if pointer < base:
            raise Exception(f"Stack {stack} is empty")

        data = self.stacks[pointer]
        self.stacks[pointer] = None
        self.pointer_mapping[stack] -= 1
        return data


def test_array_stacks():
    stacks = ArrayStacks()

    # Push to each stack
    stacks.push(10, "1")
    stacks.push(20, "2")
    stacks.push(30, "3")

    assert stacks.pop("1") == 10
    assert stacks.pop("2") == 20
    assert stacks.pop("3") == 30

    # Test multiple pushes and pops
    for i in range(5):
        stacks.push(i, "1")
    for i in reversed(range(5)):
        assert stacks.pop("1") == i

    # Test overflow
    try:
        for i in range(11):
            stacks.push(i, "2")
        assert False, "Should have raised overflow"
    except Exception as e:
        assert str(e) == "Stack 2 is full capacity"

    # Test underflow
    try:
        stacks.pop("3")
        assert False, "Should have raised underflow"
    except Exception as e:
        assert str(e) == "Stack 3 is empty"

    # Test invalid stack id
    try:
        stacks.push(42, "4")
        assert False, "Should have raised invalid stack"
    except Exception as e:
        assert str(e) == "Invalid stack id"

    print("✅ All tests passed.")

if __name__ == "__main__":
    test_array_stacks()
