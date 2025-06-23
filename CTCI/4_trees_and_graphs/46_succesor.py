from typing import Optional
from CTCI.helpers.trees import TreeNode

# solution assuming nodes has a ref to their parent (this is what CTCI asks for)
# def successor(node: TreeNode) -> Optional[TreeNode]:
#     if node.right:
#         current = node.right
#         while current.left:
#             current = current.left
#         return current
#     else:
#         parent = node.parent
#         while parent is not None and node == parent.right:
#             node = parent
#             parent = parent.parent
#         return parent
#
# Without parent ref
def successor(root: TreeNode, target: TreeNode) -> Optional[TreeNode]:
    if target.right:
        curr = target.right
        while curr.left:
            curr = curr.left
        return curr

    succ = None
    curr = root
    while curr:
        if target.data < curr.data:
            succ = curr
            curr = curr.left
        elif target.data > curr.data:
            curr = curr.right
        else:
            break

    return succ


def test_successor():
    # Build the tree manually
    #        20
    #       /  \
    #     10    30
    #    /  \
    #   5   15
    #      /
    #     13

    n20 = TreeNode(20)
    n10 = TreeNode(10)
    n30 = TreeNode(30)
    n5 = TreeNode(5)
    n15 = TreeNode(15)
    n13 = TreeNode(13)

    # Connect nodes
    n20.left = n10
    n20.right = n30
    n10.left = n5
    n10.right = n15
    n15.left = n13

    # Optional: Add parent references if your solution uses them
    for parent, child in [
        (n20, n10), (n20, n30), (n10, n5), (n10, n15), (n15, n13)
    ]:
        if child:
            child.parent = parent

    # Test successors
    assert successor(n20, n5).data == 10     # after 5 is 10
    assert successor(n20, n10).data == 13    # after 10 is 13
    assert successor(n20, n13).data == 15    # after 13 is 15
    assert successor(n20, n15).data == 20    # after 15 is 20
    assert successor(n20, n20).data == 30    # after 20 is 30
    assert successor(n20, n30) is None       # 30 has no successor

    print("✅ All successor() test cases passed.")

if __name__ == '__main__':
    test_successor()
