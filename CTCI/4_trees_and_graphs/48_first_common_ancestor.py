from typing import Optional
from CTCI.helpers.trees import TreeNode

def first_common_ancestor(root: Optional[TreeNode], n1: Optional[TreeNode], n2: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None

    if n1 == n2:
        return n1

    if root == n1 or root == n2:
        return root

    left = first_common_ancestor(root.left, n1, n2)
    right = first_common_ancestor(root.right, n1, n2)

    if left and right:
        # root is the common ancestor
        return root

    return left if left else right


def test_first_common_ancestor():
    def find(root, val):
        """Helper to find a TreeNode by value (used in tests)."""
        if root is None:
            return None
        if root.data == val:
            return root
        return find(root.left, val) or find(root.right, val)

    # Example 1
    A = TreeNode("A")
    B = TreeNode("B")
    C = TreeNode("C")
    D = TreeNode("D")
    E = TreeNode("E")
    F = TreeNode("F")
    A.left, A.right = B, C
    B.left, B.right = D, E
    C.right = F

    assert first_common_ancestor(A, D, E).data == "B"
    assert first_common_ancestor(A, D, F).data == "A"
    assert first_common_ancestor(A, B, F).data == "A"
    assert first_common_ancestor(A, B, E).data == "B"

    # Example 2 (left-skewed)
    A = TreeNode("A")
    B = TreeNode("B")
    C = TreeNode("C")
    D = TreeNode("D")
    A.left = B
    B.left = C
    C.left = D

    assert first_common_ancestor(A, C, D).data == "C"
    assert first_common_ancestor(A, B, D).data == "B"
    assert first_common_ancestor(A, A, D).data == "A"

    # Example 3 (right-skewed)
    A = TreeNode("A")
    B = TreeNode("B")
    C = TreeNode("C")
    D = TreeNode("D")
    A.right = B
    B.right = C
    C.right = D

    assert first_common_ancestor(A, C, D).data == "C"
    assert first_common_ancestor(A, B, C).data == "B"

    # Example 4 (uneven depths)
    A = TreeNode("A")
    B = TreeNode("B")
    C = TreeNode("C")
    D = TreeNode("D")
    E = TreeNode("E")
    F = TreeNode("F")
    G = TreeNode("G")
    A.left, A.right = B, C
    B.left = D
    C.left, C.right = E, F
    F.left = G

    assert first_common_ancestor(A, D, E).data == "A"
    assert first_common_ancestor(A, E, G).data == "C"
    assert first_common_ancestor(A, G, F).data == "F"

    print("✅ All tests for first_common_ancestor passed!")

if __name__ == '__main__':
    test_first_common_ancestor()
