from typing import Optional
from CTCI.helpers.trees import TreeNode

# [1, 2, 3, 4, 5, 6, 7]
# Find the mid of the input arr
# Do something similar to a binary search

def create_minimal_tree(arr: list[int]) -> Optional[TreeNode]:
    n = len(arr)
    if n == 0:
        return None

    if n == 1:
        return TreeNode(arr[0])

    pivot = n // 2
    root = TreeNode(arr[pivot])
    root.left = create_minimal_tree(arr[0: pivot])
    root.right = create_minimal_tree(arr[pivot + 1: n])
    return root

def test_minimal_tree():
    def in_order(node):
        if not node:
            return []
        return in_order(node.left) + [node.data] + in_order(node.right)

    test_cases = [
        ([], []),                       # empty tree
        ([1], [1]),                     # single element
        ([1, 2], [1, 2]),               # two elements
        ([1, 2, 3], [1, 2, 3]),         # perfect small BST
        ([1, 2, 3, 4], [1, 2, 3, 4]),   # even number of nodes
        ([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]),  # 3-level full BST
        ([10, 20, 30, 40, 50], [10, 20, 30, 40, 50]),    # non-trivial values
    ]

    for i, (arr, expected) in enumerate(test_cases):
        root = create_minimal_tree(arr)
        actual = in_order(root)
        assert actual == expected, f"Test {i} failed: expected {expected}, got {actual}"

    print("✅ All minimal_tree tests passed.")

if __name__ == '__main__':
    test_minimal_tree()
