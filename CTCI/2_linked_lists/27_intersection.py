from CTCI.helpers.linked_list import LinkedListNode, generate_list, print_list, attach


def intersection(l1, l2) -> bool:
    len_1, len_2, p1, p2 = 0, 0, l1, l2

    while p1 or p2:
        if p1:
            len_1 += 1
            p1 = p1.next
        if p2:
            len_2 += 1
            p2 = p2.next

    diff = abs(len_1 - len_2)

    if len_1 > len_2:
        longer, shorter = l1, l2
    elif len_1 < len_2:
        longer, shorter = l2, l1
    else:
        longer, shorter = l1, l2

    while diff > 0:
        longer = longer.next
        diff -= 1

    while longer is not shorter:
        longer = longer.next
        shorter = shorter.next

    return longer is not None and shorter is not None

def test_solution(l1: LinkedListNode, l2: LinkedListNode, expected):
    actual = intersection(l1, l2)
    assert actual == expected, f"Got {actual} for intersection between {print_list(l1)} and {print_list(l2)}, expected {expected}"

if __name__ == '__main__':
    shared = generate_list([5, 6, 7])

    data_set = [
        [
           attach(generate_list([1, 2, 3, 4]), shared),
           attach(generate_list([10, 15, 20]), shared),
           True
        ],
        [
            generate_list([1, 2, 3, 4]),
            generate_list([10, 15, 20]),
            False
        ],
        [
            generate_list([1, 2, 3, 4]),
            generate_list([1, 2, 3, 4]),
            False
        ],
        [
            None,
            generate_list([1, 2, 3, 4]),
            False
        ],
        [
            generate_list([]),
            generate_list([1, 2, 3, 4]),
            False
        ],
        [
            generate_list([]),
            generate_list([]),
            False
        ],
    ]

    for l1, l2, expected in data_set:
        test_solution(l1, l2, expected)
