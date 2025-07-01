# def combinations(n: int):
#     if n == 0:
#         return [""]
#     result = set()
#     for i in range(n):
#         lefts = combinations(i)
#         rights = combinations(n - 1 - i)
#         for left in lefts:
#             for right in rights:
#                 result.add(f'({left}){right}')

#     return list(result)
#

def combinations(n):
    result = []
    def backtrack(current, left, right):
        if left == 0 and right == 0:
            result.append(current)
            return
        if left > 0:
            backtrack(current + "(", left - 1, right)
        if right > left:
            backtrack(current + ")", left, right - 1)
    backtrack("", n, n)
    return result


# if n == 1 -> ()
# if n == 2 -> ()() - (())
# if n == 3 -> ()()() - ((())) - (()()) - (())() - ()(())


if __name__ == '__main__':
    print(combinations(3))
