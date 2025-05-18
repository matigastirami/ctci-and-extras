def partition_list(head, partition):
    # First found the partition exists in the list
    pivot = head
    pivot_pos = 0
    while pivot:
        if pivot.data != partition:
            pivot = pivot.next
            pivot_pos += 1

    # If not found return None
    if not pivot:
        return None

    iterator = head
    curr_pos = 0

    # pivot_pos = 1
    # 3 - 5 (pivot) - 8 - 5 - 10 - 2 - 3 - None

    while iterator:
        if iterator.data < pivot.data and curr_pos > pivot_pos:
            

        curr_pos += 1
        iterator = iterator.next
