# def count_ways(n: int) -> int:
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n == 3:
#         return 4

#     return count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 3)

# Efficient way
def count_ways(n: int) -> int:
    if n == 0:
        return 1

    memo = [0] * (n + 1)
    memo[0] = 1
    if n >= 1: memo[1] = 1
    if n >= 2: memo[2] = 2
    if n >= 3: memo[3] = 4

    for i in range(4, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]

    return memo[n]



def test_count_ways():
    data_set = [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 4),
        (4, 7),
        (5, 13),
        (10, 274),
        (20, 121415)
    ]

    for n, expected in data_set:
        actual = count_ways(n)
        assert actual == expected, f"Failed for n={n}: got {actual}, expected {expected}"

    print("✅ All count_ways tests passed!")

if __name__ == '__main__':
    test_count_ways()
