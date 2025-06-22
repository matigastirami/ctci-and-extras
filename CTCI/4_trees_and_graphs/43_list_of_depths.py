from CTCI.helpers.linked_list import LinkedListNode
from CTCI.helpers.trees import TreeNode
from CTCI.helpers.queues import Queue

# TODO: finish debugging this
def list_of_depths(root: TreeNode):
    lists = {}
    if root is None:
        return None
    queue = Queue()
    queue.push({"node": root, "level": 0})

    while not queue.is_empty():
        elem = queue.pop()
        curr_level = elem["level"]

        if not str(curr_level) in lists:
            lists[str(curr_level)] = LinkedListNode(elem["node"])
        else:
            lists[str(curr_level)].insert_end(elem["node"])

        if elem['node'].left is not None:
            queue.push({"node": elem['node'].left, "level": elem["level"] + 1})
        if elem['node'].right is not None:
            queue.push({"node": elem['node'].right, "level": elem["level"] + 1})

    return lists

def collect_levels_as_lists(levels: dict) -> dict:
    """Converts LinkedListNode levels into plain Python lists for easier assertions."""
    result = {}
    for level, node in levels.items():
        result[level] = []
        while node:
            result[level].append(node.data)  # assuming node.data is a TreeNode
            node = node.next
    return result


def test_list_of_depths():
    # Test 1: Empty Tree
    assert list_of_depths(None) is None

    # Test 2: Single Node
    root = TreeNode(1)
    levels = list_of_depths(root)
    assert collect_levels_as_lists(levels) == {'0': [1]}

    # Test 3: Two-Level Tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    levels = list_of_depths(root)
    assert collect_levels_as_lists(levels) == {'0': [1], '1': [2, 3]}

    # Test 4: Left-heavy Tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    levels = list_of_depths(root)
    assert collect_levels_as_lists(levels) == {'0': [1], '1': [2], '2': [3]}

    # Test 5: Full 3-Level Tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    levels = list_of_depths(root)
    assert collect_levels_as_lists(levels) == {
        '0': [4],
        '1': [2, 6],
        '2': [1, 3, 5, 7]
    }

    print("✅ All list_of_depths tests passed.")

if __name__ == '__main__':
    test_list_of_depths()
