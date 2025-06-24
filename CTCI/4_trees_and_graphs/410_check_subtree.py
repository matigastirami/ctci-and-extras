from typing import Optional
from CTCI.helpers.trees import TreeNode

def pre_order(node: Optional[TreeNode]) -> list:
    if not node:
        return [None]
    return [node.data] + pre_order(node.left) + pre_order(node.right)

def is_sublist(l1: list, l2: list) -> bool:
    n, m = len(l1), len(l2)
    for i in range(m - n + 1):
        if l2[i:i+n] == l1:
            return True
    return False

def check_subtree(n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
    p1 = pre_order(n1)
    p2 = pre_order(n2)
    return is_sublist(p2, p1)


def test_check_subtree():
    # Helper function to build a small tree
    def build_tree_from_list(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    # Test 1: T2 is a subtree of T1
    t1 = build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    t2 = build_tree_from_list([2, 4, 5])
    assert check_subtree(t1, t2) == True

    # Test 2: T2 is not a subtree of T1
    t1 = build_tree_from_list([1, 2, 3])
    t2 = build_tree_from_list([2, 3])
    assert check_subtree(t1, t2) == False

    # Test 3: T2 is identical to T1
    t1 = build_tree_from_list([1, 2, 3])
    t2 = build_tree_from_list([1, 2, 3])
    assert check_subtree(t1, t2) == True

    # Test 4: T2 is None (should always be a subtree)
    t1 = build_tree_from_list([1, 2, 3])
    assert check_subtree(t1, None) == True

    # Test 5: T1 is None, T2 is not (T2 can't be subtree)
    t2 = build_tree_from_list([1])
    assert check_subtree(None, t2) == False

    # Test 6: Deep subtree
    t1 = build_tree_from_list([1, 2, 3, None, None, 4, 5])
    t2 = build_tree_from_list([3, 4, 5])
    assert check_subtree(t1, t2) == True

    print("✅ All check_subtree test cases passed.")

if __name__ == "__main__":
    test_check_subtree()
