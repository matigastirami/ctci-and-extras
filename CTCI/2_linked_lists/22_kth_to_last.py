# Approach: First count the total elements, then iterate until total - k
from helpers.linked_list import Node

def kth_to_last(head, k):
    curr = head
    total_nodes = 0
    while curr:
        total_nodes += 1
        curr = curr.next

    if total_nodes < k:
        return None

    down_counter = total_nodes - k
    curr = head
    while down_counter > 0:
        curr = curr.next
        down_counter -= 1

    return curr

def print_kth_to_last(head, k):
    elem = kth_to_last(head, k)
    print(elem.data if elem is not None else 'None')

if __name__ == "__main__":
    # Building the list: 10 -> 20 -> 30 -> 40 -> 50
    linked_list = Node(10)
    linked_list.head = linked_list
    linked_list.insert_end(20)
    linked_list.insert_end(30)
    linked_list.insert_end(40)
    linked_list.insert_end(50)

    # Test cases
    print("Linked list:")
    current = linked_list.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print_kth_to_last(linked_list, 1)  # Expect 50
    print_kth_to_last(linked_list, 2)  # Expect 40
    print_kth_to_last(linked_list, 3)  # Expect 30
    print_kth_to_last(linked_list, 5)  # Expect 10
    print_kth_to_last(linked_list, 6)  # Expect None or error
