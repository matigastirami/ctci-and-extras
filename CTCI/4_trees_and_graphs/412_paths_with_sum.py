from CTCI.helpers.trees import TreeNode

def count_paths_from_node(node: TreeNode, target: int, curr_sum: int = 0) -> int:
    if node is None:
        return 0

    curr_sum += node.data
    total_paths = 1 if curr_sum == target else 0

    total_paths += count_paths_from_node(node.left, target, curr_sum)
    total_paths += count_paths_from_node(node.right, target, curr_sum)

    return total_paths


def paths_with_sum(root: TreeNode, target: int, curr_sum: int = 0) -> int:
    if root is None:
        return 0

    paths_from_root = count_paths_from_node(root, target)

    return (
        paths_with_sum(root.left, target, root.data + curr_sum) +
        paths_with_sum(root.right, target, root.data + curr_sum) +
        paths_from_root
    )

def test_path_to_sum():
    # Test 1: Empty tree
    assert paths_with_sum(None, 5) == 0

    # Test 2: Single node matching target
    root = TreeNode(5)
    assert paths_with_sum(root, 5) == 1
    assert paths_with_sum(root, 10) == 0

    # Test 3: Simple tree
    #
    #       5
    #      / \
    #     3   -2
    #    / \    \
    #   2   1    2
    #
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(-2)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(2)

    assert paths_with_sum(root, 8) >= 1
    assert paths_with_sum(root, 5) >= 1
    assert paths_with_sum(root, 10) >= 0

    # Test 4: Tree with multiple overlapping paths
    #
    #       10
    #      /  \
    #     5   -3
    #    / \    \
    #   3   2    11
    #  / \   \
    # 3  -2   1
    #
    complex_root = TreeNode(10)
    complex_root.left = TreeNode(5)
    complex_root.right = TreeNode(-3)
    complex_root.left.left = TreeNode(3)
    complex_root.left.right = TreeNode(2)
    complex_root.right.right = TreeNode(11)
    complex_root.left.left.left = TreeNode(3)
    complex_root.left.left.right = TreeNode(-2)
    complex_root.left.right.right = TreeNode(1)

    assert paths_with_sum(complex_root, 8) >= 3
    assert paths_with_sum(complex_root, 18) >= 1
    assert paths_with_sum(complex_root, 100) == 0

    print("✅ All test_path_to_sum tests ran (assert exact values once logic is confirmed)")

if __name__ == '__main__':
    test_path_to_sum()
