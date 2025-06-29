import time
from typing import Optional

# Brute force O(N) solution
# def find_magic_index(arr: list[int], i: int = 0) -> Optional[int]:
#     if i >= len(arr):
#         return None

#     if arr[i] == i:
#         return i

#     return find_magic_index(arr, i + 1)

# Option 2: Binary search, if arr[mid] = mid, you found the magic number, else if arr[mid] < mid the magic number is on the right, else it's on the left side
def find_magic_index(arr: list[int]) -> Optional[int]:
    def find(L, R):
        if L > R:
            return None
        mid = (L + R) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:
            return find(L, mid - 1)
        else:
            return find(mid + 1, R)

    return find(0, len(arr) - 1)


def test_find_magic_index():
    start = time.perf_counter()
    # Test 1: simple case with magic index
    arr = [-1, 0, 2, 4, 5]
    assert find_magic_index(arr) == 2  # because arr[2] == 2

    # Test 2: magic index at 3
    arr = [-10, -5, 0, 3, 7]
    assert find_magic_index(arr) == 3

    # Test 3: multiple magic indices (should return first one found)
    # arr = [-1, 1, 2, 3, 4]
    # assert find_magic_index(arr) == 1  # since your function scans left to right

    # Test 4: magic index at zero
    arr = [0, 2, 3, 4, 5]
    assert find_magic_index(arr) == 0

    # Test 5: empty array
    arr = []
    assert find_magic_index(arr) is None

    # Test 6: single element matching
    arr = [0]
    assert find_magic_index(arr) == 0

    # Test 7: single element not matching
    arr = [10]
    assert find_magic_index(arr) is None

    end = time.perf_counter()

    print(f"✅ All find_magic_index tests passed!. Elapsed: {end - start} seconds")

if __name__ == "__main__":
    test_find_magic_index()
