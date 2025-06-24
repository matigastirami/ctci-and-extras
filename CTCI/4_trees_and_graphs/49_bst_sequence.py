from CTCI.helpers.trees import TreeNode
from typing import Optional, List

def weave_lists(first, second, prefix, results):
    if not first or not second:
        result = prefix + first + second
        results.append(result)
        return

    head_first = first[0]
    weave_lists(first[1:], second, prefix + [head_first], results)

    head_second = second[0]
    weave_lists(first, second[1:], prefix + [head_second], results)

def bst_sequences(node: Optional[TreeNode]):
    if node is None:
        return [[]]

    result = []
    left_seqs = bst_sequences(node.left)
    right_seqs = bst_sequences(node.right)

    for left in left_seqs:
        for right in right_seqs:
            weaved = []
            weave_lists(left, right, prefix=[node.data], results=weaved)
            result.extend(weaved)

    return result

def test_bst_sequences():
    def extract_sequences(sequences: List[List[int]]) -> List[str]:
        return sorted(["->".join(map(str, seq)) for seq in sequences])

    # Test 1: Empty tree
    assert bst_sequences(None) == [[]]

    # Test 2: Single node
    root = TreeNode(1)
    assert bst_sequences(root) == [[1]]

    # Test 3: Two nodes, left child only
    root = TreeNode(2)
    root.left = TreeNode(1)
    assert bst_sequences(root) == [[2, 1]]

    # Test 4: Two nodes, right child only
    root = TreeNode(2)
    root.right = TreeNode(3)
    assert bst_sequences(root) == [[2, 3]]

    # Test 5: Three nodes - root with both children
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    output = bst_sequences(root)
    expected = [
        [2, 1, 3],
        [2, 3, 1]
    ]
    assert sorted(output) == sorted(expected)

    # Test 6: Three-level balanced tree
    #         2
    #        / \
    #       1   3
    #            \
    #             4
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    output = bst_sequences(root)
    result = extract_sequences(output)
    assert any("2->1->3->4" in r for r in result)
    assert any("2->3->1->4" in r for r in result)
    assert all(seq[0] == 2 for seq in output)

    # Test 7: Degenerate tree (like a linked list)
    # 1 -> 2 -> 3 -> 4
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    output = bst_sequences(root)
    assert output == [[1, 2, 3, 4]]  # Only one valid sequence

    print("✅ All bst_sequences tests passed.")

if __name__ == '__main__':
    test_bst_sequences()
