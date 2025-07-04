from CTCI.helpers.trees import TreeNode
from shutil import posix

# Most naive implementation O(n^2)
# def height(root: TreeNode) -> int:
#     if not root:
#         return 0

#     return height(root.left) + height(root.right) + 1

# def is_balanced(root: TreeNode) -> bool:
#     if not root:
#         return True

#     lh = height(root.left)
#     rh = height(root.right)

#     return abs(lh - rh) <= 1

# More optimized solution (still recursive but O(N))
# def check_balanced(root: TreeNode) -> tuple[int, bool]:
#     if root is None:
#         return (0, True)

#     left_height, is_left_balanced = check_balanced(root.left)
#     if not is_left_balanced:
#         return (0, False)

#     right_height, is_right_balanced = check_balanced(root.right)
#     if not is_right_balanced:
#         return (0, False)

#     height = 1 + max(left_height, right_height)
#     balanced = abs(left_height - right_height) <= 1
#     return (height, balanced)

# def is_balanced(root: TreeNode) -> bool:
#     _, balanced = check_balanced(root)
#     return balanced

# Non-recursive solution using BFS
def is_balanced(root: TreeNode) -> bool:
    if root is None:
        return True

    stack = [root]
    heights = {}
    visited = set()

    while stack:
        node = stack[-1]
        if node.left and node.left not in visited:
            stack.append(node.left)
        elif node.right and node.right not in visited:
            stack.append(node.right)
        else:
            stack.pop()
            visited.add(node)
            left_height = heights.get(node.left, 0)
            right_height = heights.get(node.right, 0)
            if abs(left_height - right_height) > 1:
                return False

            heights[node] = max(left_height, right_height) + 1

    return True


def test_is_balanced():
    # Test 1: Empty tree
    assert is_balanced(None) == True

    # Test 2: Single node
    root = TreeNode(1)
    assert is_balanced(root) == True

    # Test 3: Balanced tree with 3 nodes
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert is_balanced(root) == True

    # Test 4: Left-heavy but still balanced
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right = TreeNode(4)
    assert is_balanced(root) == True

    # Test 5: Unbalanced tree (left side is 2 deeper)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.right = TreeNode(5)
    assert is_balanced(root) == False

    # Test 6: Unbalanced tree (right side is 2 deeper)
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    assert is_balanced(root) == False

    print("✅ All is_balanced tests executed.")

if __name__ == '__main__':
    test_is_balanced()
