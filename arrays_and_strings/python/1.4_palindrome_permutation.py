def is_palindrome(string: str) -> bool:
    seen = set()
    total_odd = 0

    for c in string:
        if c not in seen:
            total_odd += 1

    return total_odd == 1

# TODO: finish this, it's weird
if __name__ == '__main__':
    is_palindrome('atco cta')