# Complexity O(N) only visit characters once
def string_compression(string: str) -> str:
    i = 0
    compressed = ''

    while i < len(string):
        current_char = string[i]
        count = 1
        j = i + 1
        while j < len(string) and string[i] == string[j]:
            count += 1
            j += 1
        compressed += current_char + str(count)
        i += count

    if len(compressed) >= len(string):
        return string

    return compressed


if __name__ == '__main__':
    print(string_compression('aabcccccaaa'))
    print(string_compression('abc'))