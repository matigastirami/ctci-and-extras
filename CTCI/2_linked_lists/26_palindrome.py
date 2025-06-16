# Determine if a singly linked list is a palindrome
# Stragegies
# 1. List to string, then apply is_palindrome
# 2. Use a stack and a counter, the stack pull with provide the latest, while iterating from the beginning of the list again
#

from CTCI.helpers.linked_list import Node, generate_list, print_list

def list_to_str(head: Node) -> str:
    resp = ""
    iterator = head
    while iterator:
        resp += iterator.data
        iterator = iterator.next
    return resp

def is_palindrome(s: str) -> bool:
    n = len(s)
    for i in range(0, n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True

def is_list_palindrome(head: Node):
    string = list_to_str(head)
    return is_palindrome(string)

def test_solution(head: Node, expected):
    assert is_list_palindrome(head) == expected, f"{print_list(head)} returned a wrong value"

if __name__ == '__main__':
    data_set = [
        [generate_list(['a', 'a']), True],
        [generate_list(['a']), True],
        [generate_list([]), True],
        [generate_list(['a', 'b']), False],
        [generate_list(['a', 'b', 'a']), True],
        [generate_list(['a', 'b', 'c', 'd']), False]
    ]

    for test in data_set:
        test_solution(test[0], test[1])
