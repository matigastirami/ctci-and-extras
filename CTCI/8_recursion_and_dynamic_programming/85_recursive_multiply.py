# Linear solution O(b)
# def multiply(a, b) -> int:
#     if b == 0:
#         return 0
#     return a + multiply(a, b - 1)

# Binary solution O(log b)
def multiply(a, b) -> int:
    if b == 0:
        return 0

    half = multiply(a, b // 2)

    if b % 2 == 0:
        return half + half
    else:
        return half + half + a

if __name__ == '__main__':
    print(multiply(2, 15))
