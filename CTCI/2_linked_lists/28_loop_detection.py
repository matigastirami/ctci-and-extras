# approach #1: have a set with the visited nodes
# approach #2: fast and slow pointer

from typing import Optional
from CTCI.helpers.linked_list import LinkedListNode, generate_list
from CTCI.helpers.linked_list import create_loop


# def detect_loop(head: Node):
#     visited = set()
#     curr = head
#     while curr:
#         if curr in visited:
#             return curr
#         visited.add(curr)
#         curr = curr.next
#     return None

def detect_loop(head: LinkedListNode) -> Optional[LinkedListNode]:
    if not head:
        return None

    slow = head
    fast = head

    while slow and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow is fast:
            break
    else:
        return None

    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return slow

if __name__ == '__main__':
    data_set = [
        [generate_list([]), None],  # empty list → no loop
        [generate_list(['a']), None],  # single node → no loop
        [generate_list(['a', 'b', 'c']), None],  # no loop
        [create_loop(generate_list(['a', 'b', 'c', 'd', 'e']), 2), 'c'],  # loop at 'c'
        [create_loop(generate_list(['x', 'y', 'z']), 0), 'x'],  # loop starts at head
        [create_loop(generate_list(['1', '2', '3', '4', '5']), 4), '5'],  # loop to tail
        [create_loop(generate_list(['n', 'o', 'p', 'q']), 1), 'o'],  # middle loop
    ]

    for i, (linked_list, expected_val) in enumerate(data_set):
        node = detect_loop(linked_list)
        actual_val = node.data if node else None
        assert actual_val == expected_val, f"Test {i} failed: expected {expected_val}, got {actual_val}"
        print(f'test case {i} passed!')
