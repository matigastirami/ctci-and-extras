from helpers.linked_list import LinkedListNode, print_list

def partition_list(head, partition):
    before_head = LinkedListNode(0)
    after_head = LinkedListNode(0)

    before = before_head
    after = after_head

    current = head

    while current:
        next_node = current.next
        current.next = None
        if current.data < partition:
            before.next = current
            before = before.next
        else:
            after.next = current
            after = after.next

        current = next_node

    before.next = after_head.next

    return before_head.next


if __name__ == "__main__":
    # Building the list: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 -> None
    linked_list = LinkedListNode(3)
    linked_list.head = linked_list
    linked_list.insert_end(5)
    linked_list.insert_end(8)
    linked_list.insert_end(5)
    linked_list.insert_end(10)
    linked_list.insert_end(2)
    linked_list.insert_end(1)

    print_list(linked_list)

    partition_list(linked_list, 5)

    print_list(linked_list)
