from helpers.linked_list import Node

if __name__ == "__main__":
    # Building the list: 10 -> 20 -> 30 -> 40 -> 50
    linked_list = Node(10)
    linked_list.insert_end(20)
    linked_list.insert_end(30)
    linked_list.insert_end(40)
    linked_list.insert_end(50)

    # Test cases
    # print_kth_to_last(head, 1)  # Expect 50
    # print_kth_to_last(head, 2)  # Expect 40
    # print_kth_to_last(head, 3)  # Expect 30
    # print_kth_to_last(head, 5)  # Expect 10
    # print_kth_to_last(head, 6)  # Expect None or error