"""1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?"""

def is_unique(string: str):
    """
    Approach 1: using a dict/hash map to track the total appearances of a given character
    :param string:
    :return:
    """
    total_chars_map = {}

    for c in string:
        if c in total_chars_map:
            return False
        total_chars_map[c] = 1

    return True

def is_unique_2(string: str):
    """
    Approach 2: Not using other structures
    :param string:
    :return:
    """
    sorted_string = ''.join(sorted(string)) # O(N * log(N))

    for i, c in enumerate(sorted_string):
        if i == 0 and c == sorted_string[i + 1] \
            or i == len(sorted_string) - 1 and c == sorted_string[i - 1] \
            or i != 0 and i != len(sorted_string) - 1 and c == sorted_string[i + 1] or c == sorted_string[i - 1]:
            return False

    return True


if __name__ == '__main__':
    print(is_unique('abcde')) # True
    print(is_unique('aab')) # False
    print(is_unique('abca')) # False

    print(is_unique_2('abcde')) # True
    print(is_unique_2('aab')) # False
    print(is_unique_2('abca')) # False
