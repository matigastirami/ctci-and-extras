from CTCI.helpers.trees import TreeNode

# def is_bst(root: TreeNode, min: float = float('-inf'), max: float = float('inf')) -> bool:
#     if root is None:
#         return True

#     if root.data <= min or root.data >= max:
#         return False

#     return is_bst(root.left, min, root.data) and is_bst(root.right, root.data, max)

def is_bst(root: TreeNode) -> bool:
    if root is None:
        return True

    stack = []
    stack.append({
        'node': root,
        'min': float('-inf'),
        'max': float('inf')
    })

    while len(stack) > 0:
        elem = stack.pop()
        node, min, max = elem['node'], elem['min'], elem['max']

        if node.data <= min or node.data >= max:
            return False

        if node.left is not None:
            stack.append({
                'node': node.left,
                'min': min,
                'max': node.data
            })
        if node.right is not None:
            stack.append({
                'node': node.right,
                'min': node.data,
                'max': max
            })

    return True

def test_is_bst():
    # Empty tree
    assert is_bst(None) == True

    # Single node tree
    root = TreeNode(10)
    assert is_bst(root) == True

    # Valid BST (small)
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    assert is_bst(root) == True

    # Valid BST (larger)
    root = TreeNode(20)
    root.left = TreeNode(10)
    root.right = TreeNode(30)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(15)
    root.right.left = TreeNode(25)
    root.right.right = TreeNode(35)
    assert is_bst(root) == True

    # Invalid BST (left child greater than parent)
    root = TreeNode(10)
    root.left = TreeNode(12)
    root.right = TreeNode(15)
    assert is_bst(root) == False

    # Invalid BST (right child less than parent)
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(8)
    assert is_bst(root) == False

    # Deep invalid BST (violates rule further down)
    root = TreeNode(20)
    root.left = TreeNode(10)
    root.right = TreeNode(30)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(25)  # 25 should not be in left subtree
    assert is_bst(root) == False

    print("✅ All is_bst test cases passed.")

if __name__ == "__main__":
    test_is_bst()
