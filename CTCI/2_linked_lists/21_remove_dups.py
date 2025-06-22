from helpers.linked_list import LinkedListNode

if __name__ == "__main__":
    linked_list = LinkedListNode(1)
    linked_list.head = linked_list  # Set the head to itself to mimic list behavior

    linked_list.insert_end(1)
    linked_list.insert_end(2)
    linked_list.insert_end(3)
    linked_list.insert_end(3)
    linked_list.insert_end(4)
    linked_list.insert_end(4)
    linked_list.insert_end(4)
    linked_list.insert_end(1)
    linked_list.insert_end(5)

    print("Before removing duplicates:")
    current = linked_list.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    linked_list.remove_dups(linked_list)

    print("\nAfter removing duplicates:")
    current = linked_list.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
