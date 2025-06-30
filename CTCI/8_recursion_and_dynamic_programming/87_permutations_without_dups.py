def permutations_without_dups(word: str):
    if not word:
        return ['']

    result = []

    for i, l in enumerate(word):
        remaining = word[:i] + word[i+1:]
        perm = permutations_without_dups(remaining)
        partial = []
        for p in perm:
            partial.append(f'{l}{p}')
        result.extend(partial)

    return result

if __name__ == '__main__':
    print(permutations_without_dups('abcd'))
