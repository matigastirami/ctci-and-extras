"""1.3 URLify: there's a second param length that does not make sense in languages where handling strings is easier than C"""

def urlify(string: str, true_length: int) -> str:
    chars = []

    for i in range(true_length):
        if string[i] == ' ':
            chars.append('%20')
        else:
            chars.append(string[i])

    return ''.join(chars)

if __name__ == '__main__':
    print(urlify('Mr John Smith    ', 13))