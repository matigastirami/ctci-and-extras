from helpers.linked_list import Node, print_list

"""
7 -> 1 -> 6 -> None
5 -> 9 -> 2 -> None
initial carry = 0
result = 2 -> 1 -> 9 -> None,
7 + 5 -> 12 -> carry = 1 and result.data = sum - 10 = 2
1 + 9 -> 10 + carry = 11 -> carry = 1 and result.data = sum - 10 = 1
6 + 2 + carry = 9 -> 9 < 10 -> carry = 0 && result.data = sum
"""

def sum_lists(l1: Node, l2: Node) -> Node:
    sum_list = Node(-1)
    result = sum_list
    carry = 0

    while l1 or l2:
        val1 = l1.data if l1 else 0
        val2 = l2.data if l2 else 0
        sum = val1 + val2 + carry

        if sum > 9:
            result.next = Node(sum - 10)
            carry = 1
        else:
            result.next = Node(sum)
            carry = 0

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        result = result.next

    if carry:
        result.next = Node(carry)

    return sum_list.next

def generate_list(values = [1, 2, 3, 4, 5]):
    dummy = Node(-1)
    current = dummy
    for val in values:
        current.next = Node(val)
        current = current.next

    return dummy.next

def test_solution(l1, l2, expected):
    list1 = generate_list(l1)
    list2 = generate_list(l2)
    result = sum_lists(list1, list2)
    expect = generate_list(expected)
    assert result == expect, f"Failed for {print_list(list1)} + {print_list(list2)}, expected {print_list(expect)}, got {print_list(result)}"

if __name__ == '__main__':
    # Basic test from the book
    test_solution([7, 1, 6], [5, 9, 2], [2, 1, 9])  # 617 + 295 = 912

    # Both lists are empty
    test_solution([], [], [])

    # One list is empty
    test_solution([1, 2, 3], [], [1, 2, 3])
    test_solution([], [9, 9, 9], [9, 9, 9])

    # Different lengths without carry
    test_solution([1, 2], [3], [4, 2])  # 21 + 3 = 24

    # Different lengths with carry
    test_solution([9, 9], [1], [0, 0, 1])  # 99 + 1 = 100

    # Carry causes an extra digit
    test_solution([9, 9, 9], [1], [0, 0, 0, 1])  # 999 + 1 = 1000

    # All carry
    test_solution([5, 5, 5], [5, 5, 5], [0, 1, 1, 1])  # 555 + 555 = 1110

    # Ends in multiple carries
    test_solution([2, 9], [8, 1], [0, 1, 1])  # 92 + 18 = 110

    # Large inputs
    # TODO: check this particular case, maybe it's wrong
    # test_solution([1]*20, [9]*20, [0]*20 + [2])  # 111...1 + 999...9 = 111...0 (2 at the end)

    # Very small inputs
    test_solution([0], [0], [0])
