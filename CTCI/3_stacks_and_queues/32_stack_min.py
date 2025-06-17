# Each node is aware of the min of its substack
class StackMinNode:
    def __init__(self, data, min) -> None:
        super().__init__()
        self.data = data
        self.min = min
        self.next = None

class StackMin:
    def __init__(self) -> None:
        self.top = None

    def push(self, data):
        min_val = data if not self.top else min(data, self.top.min)
        node = StackMinNode(data, min_val)
        node.next = self.top
        self.top = node

    def get_min(self):
        return self.top.min if self.top else None

    def pop(self):
        if not self.top:
            return None
        node = self.top
        self.top = node.next
        return node.data

def test_stack_min():
    s = StackMin()

    # Push and check min
    s.push(5)
    assert s.get_min() == 5

    s.push(6)
    assert s.get_min() == 5  # min should remain 5

    s.push(3)
    assert s.get_min() == 3  # new min

    s.push(7)
    assert s.get_min() == 3  # min still 3

    s.push(2)
    assert s.get_min() == 2  # new min

    # Pop and check min
    assert s.pop() == 2
    assert s.get_min() == 3

    assert s.pop() == 7
    assert s.get_min() == 3

    assert s.pop() == 3
    assert s.get_min() == 5  # min should update correctly

    assert s.pop() == 6
    assert s.get_min() == 5

    assert s.pop() == 5
    assert s.get_min() == None  # should be safe when empty

    # Test pop on empty stack
    assert s.pop() == None

    print("all tests passed")

if __name__ == '__main__':
    test_stack_min()
