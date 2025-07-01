# def make_change(n: int, coins = [25, 10, 5, 1], result = None) -> int:
#     if result is None:
#         result = 0
#     if n < 0:
#         return 0
#     if n == 0:
#         return 1
#     for i in range(len(coins)):
#         result += make_change(n - coins[i], coins[i:])

#     return result

# Cleaner approach
def make_change(n, coins = [25, 10, 5, 1], index=0):
    if n == 0:
        return 1
    if n < 0 or index == len(coins):
        return 0

    with_coin = make_change(n - coins[index], coins, index) # Count all the possibilities that includes the coin at index
    without_coin = make_change(n, coins, index + 1) # Count all the possibilities that don't include the coin at index
    return with_coin + without_coin


if __name__ == '__main__':
    print(make_change(25))
    print(make_change(26))
    print(make_change(32))
    print(make_change(5))
    print(make_change(2))
