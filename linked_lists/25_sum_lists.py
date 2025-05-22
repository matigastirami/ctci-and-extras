from helpers.linked_list import Node

def sum_lists(l1: Node, l2: Node) -> Node:
    sum_list = Node(-1)
    result = sum_list
    carry = 0

    while l1 and l2:
        sum = l1.data + l2.data
        sum_list.next = sum if sum < 10 else

    return sum_list

if __name__ == '__main__':
    l1 = Node(7)
    l1.head = l1
    l1.insert_end(1)
    l1.insert_end(6)

    l1 = Node(5)
    l1.head = l1
    l1.insert_end(9)
    l1.insert_end(2)
