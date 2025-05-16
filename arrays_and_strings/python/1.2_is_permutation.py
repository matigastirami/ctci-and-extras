"""1.2 Given 2 strings write a method to decide if one is a permutation of the other"""
from collections import Counter


def is_permutation(str1: str, str2: str):
    if len(str1) != len(str2):
        return False

    str1_sort = sorted(str1)
    str2_sort = sorted(str2)

    return str1_sort == str2_sort

# A cleaner O(N) solution
def is_permutation_2(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False

    return Counter(str1) == Counter(str2)

if __name__ == '__main__':
    print(is_permutation('abcd', 'dcba')) # True
    print(is_permutation('abc', 'ab')) # False
    print(is_permutation('bahia', 'habia')) # True