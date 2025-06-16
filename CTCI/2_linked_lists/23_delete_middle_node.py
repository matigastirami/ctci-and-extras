from helpers.linked_list import print_list, Node

def delete_middle_node(node_ref):
    # As I don't have the prev node ref, I can't unlink and attach to the next, so the strategy would be copying next data to current and then unlink the next
    if not node_ref:
        raise Exception('node_ref cannot be None')

    node_ref.data = node_ref.next.data
    node_ref.next = node_ref.next.next

if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    linked_list = Node(1)
    current = linked_list
    for i in range(2, 6):
        current.next = Node(i)
        current = current.next

    print("Original list:")
    print_list(linked_list)

    # Let's simulate being given only node 3
    node_to_delete = linked_list.next.next  # This is the node with data=3
    print(f"\nTarget node to 'delete': {node_to_delete.data}")

    # Here you'd call your delete-in-the-middle function
    # Example: delete_middle_node(node_to_delete)
    delete_middle_node(linked_list.next.next.next)

    print("\nList after deletion (expected: 1 -> 2 -> 4 -> 5):")
    print_list(linked_list)
