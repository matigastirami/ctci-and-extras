# This is a less efficient implementation based on exercise 8.7 but using a set instead of a list, CTCI expects you to use a frequency counter
# def permutations(word: str):
#     if not word:
#         return ['']

#     result = set()

#     for i, l in enumerate(word):
#         remaining = word[:i] + word[i+1:]
#         perm = permutations(remaining)
#         for p in perm:
#             result.add(f'{l}{p}')

#     return list(result)

# CTCI way
def permutations(word: str):
    def backtrack(counter, prefix, remaining, result):
        if remaining == 0:
            result.append(prefix)
            return

        for char in counter:
            if counter[char] > 0:
                counter[char] -= 1
                backtrack(counter, prefix + char, remaining - 1, result)
                counter[char] += 1

    frequencies = {}
    for l in word:
        if l not in frequencies:
            frequencies[l] = 0

        frequencies[l] += 1
    result = []
    backtrack(frequencies, '', len(word), result)
    return result


if __name__ == '__main__':
    print(permutations('aba'))
