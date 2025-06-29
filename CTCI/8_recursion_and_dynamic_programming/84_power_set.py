# def power_set(nums: list):
#     if not nums:
#         return [[]]

#     first = nums[0]
#     rest_power_set = power_set(nums[1:])

#     with_first = []
#     for subset in rest_power_set:
#         with_first.append([first] + subset)

#     return rest_power_set + with_first

def power_set(nums: list):
    result = [[]]
    for num in nums:
        new_subsets = []
        for subset in result:
            new_subsets.append(subset + [num])
        result.extend(new_subsets)
    return result

def test_power_set():
    # Helper to compare ignoring order
    def same_power_set(a, b):
        return sorted([sorted(x) for x in a]) == sorted([sorted(x) for x in b])

    # Test 1: empty set
    assert same_power_set(power_set([]), [[]])

    # Test 2: one element
    assert same_power_set(power_set([1]), [[], [1]])

    # Test 3: two elements
    expected = [[], [1], [2], [1,2]]
    assert same_power_set(power_set([1,2]), expected)

    # Test 4: three elements
    expected = [
        [], [1], [2], [3],
        [1,2], [1,3], [2,3],
        [1,2,3]
    ]
    assert same_power_set(power_set([1,2,3]), expected)

    print("All tests passed!")

if __name__ == '__main__':
    test_power_set()
