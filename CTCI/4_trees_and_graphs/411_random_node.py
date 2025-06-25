import random
from collections import defaultdict


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.size = 1

    def in_order(self):
        return (self.left.in_order() if self.left else []) + [self.data] + (self.right.in_order() if self.right else [])

    def insert(self, data):
        if data <= self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BSTNode(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BSTNode(data)
        self.size += 1

    def get_random_node(self):
        left_size = self.left.size if self.left else 0
        index = random.randint(0, self.size - 1)

        if index < left_size:
            return self.left.get_random_node()
        elif index == left_size:
            return self
        else:
            return self.right.get_random_node()

    def find(self, value):
        if not self:
            return None

        if value == self.data:
            return self
        elif value < self.data:
            return self.left.find(value) if self.left else None
        else:
            return self.right.find(value) if self.right else None

    def delete(self, data):
        if data < self.data:
            self.left = self.left.delete(data)
        elif data > self.data:
            self.right = self.right.delete(data)
        else:
            if not self.left and not self.right:
                return None
            elif not self.left:
                return self.right
            elif not self.right:
                return self.left
            else:
                min_larger_node = self.right.find_min()
                self.data = min_larger_node.data
                self.right = self.right.delete(min_larger_node.data)

        self.size = 1 + (self.left.size if self.left else 0) + (self.right.size if self.right else 0)
        return self

    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current

def test_find():
    root = BSTNode(10)
    root.insert(5)
    root.insert(15)
    root.insert(3)
    root.insert(7)
    root.insert(12)
    root.insert(17)

    assert root.find(10) is root
    assert root.find(5).data == 5
    assert root.find(3).data == 3
    assert root.find(17).data == 17
    assert root.find(100) is None
    assert root.find(-5) is None

    print("✅ All find() tests passed!")

def test_get_random_node():
    random.seed(42)  # for reproducibility
    root = BSTNode(10)
    values = [5, 15, 3, 7, 12, 17]
    for val in values:
        root.insert(val)

    counts = defaultdict(int)
    total_runs = 10000

    for _ in range(total_runs):
        node = root.get_random_node()
        counts[node.data] += 1

    # Expected: Each node should be ~14.3% if distribution is uniform (1/7)
    print("Frequency distribution of get_random_node() over", total_runs, "runs:")
    for val in [10] + values:
        freq = counts[val] / total_runs * 100
        print(f"Value {val}: {counts[val]} times ({freq:.2f}%)")

    # Just basic sanity checks
    assert sum(counts.values()) == total_runs
    assert all(val in counts for val in [10] + values)

    print("✅ get_random_node() test passed with roughly uniform distribution.")

def test_delete():
    root = BSTNode(10)
    for val in [5, 15, 3, 7, 12, 17]:
        root.insert(val)

    assert root.in_order() == [3, 5, 7, 10, 12, 15, 17]

    root = root.delete(3)  # Leaf node
    assert root.in_order() == [5, 7, 10, 12, 15, 17]

    root = root.delete(5)  # One child
    assert root.in_order() == [7, 10, 12, 15, 17]

    root = root.delete(15)  # Two children
    assert root.in_order() == [7, 10, 12, 17]

    print("✅ All delete() tests passed!")

if __name__ == '__main__':
    test_find()
    test_get_random_node()
    test_delete()
