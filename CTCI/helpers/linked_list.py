class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        # current = self.head
        # ret = ''
        # while current:
        #     print(current.data, end=" -> ")
        #     ret += str(current.data) + ' -> '
        #     current = current.next

        # ret += "None"
        # return ret
        return str(self.data)

    def __repr__(self) -> str:
        return str(self.data)

    def __eq__(self, other):
        if not isinstance(other, LinkedListNode):
            return NotImplemented
        a, b = self, other
        while a and b:
            if a.data != b.data:
                return False
            a, b = a.next, b.next
        return a is None and b is None

    def __hash__(self) -> int:
        return id(self) # id is the hash representation of the memory address

    def insert_start(self, data):
        new_node = LinkedListNode(data)
        if not self.head:
            self.head
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_end(self, data):
        new_node = LinkedListNode(data)
        current_node = self
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        return self

    def remove_at_position(self, position):
        pass

    # Don't assume the list is sorted
    def remove_dups(self, node):
        current_node = node.head
        while current_node:
            iterator = current_node
            # This while would not be necessary if the list is sorted
            while iterator.next:
                if current_node.data == iterator.next.data:
                    iterator.next = iterator.next.next
                else:
                    iterator = iterator.next

            current_node = current_node.next

def print_list(head):
    current = head
    result = ""
    while current:
        result += str(current.data) + " -> "
        current = current.next

    result += "None"
    return result

def generate_list(values = [1, 2, 3, 4, 5]) -> LinkedListNode:
    dummy = LinkedListNode(-1)
    current = dummy
    for val in values:
        current.next = LinkedListNode(val)
        current = current.next

    return dummy.next

def attach(head: LinkedListNode, tail: LinkedListNode) -> LinkedListNode:
    if not head:
        return tail
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = tail
    return head

def create_loop(head: LinkedListNode, pos: int) -> LinkedListNode:
    if not head or pos < 0:
        return head

    loop_start = head
    last = head
    index = 0

    while index < pos and loop_start.next:
        loop_start = loop_start.next
        index += 1

    while last.next:
        last = last.next

    last.next = loop_start
    return head
