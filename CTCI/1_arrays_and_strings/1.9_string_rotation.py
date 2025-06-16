def string_rotation(str1:str, str2: str):
    if len(str1) != len(str2) or not str1:
        return False
    return substring(s1 + s1, s2)

def substring(s1, s2):
    return s2 in s1

if __name__ == "__main__":
    test_cases = [
        ("waterbottle", "erbottlewat", True),
        ("hello", "lohel", True),
        ("hello", "helol", False),
        ("", "", False),  # empty strings are not considered valid rotations in CTCI
        ("a", "a", True),
        ("abcd", "bcda", True),
        ("abcd", "cdab", True),
        ("abcd", "dabc", True),
        ("abcd", "acbd", False),
        ("rotation", "tationro", True),
        ("rotation", "ationrot", True),
        ("rotation", "tionrota", True),
        ("rotation", "ationtor", False),
    ]

    for s1, s2, expected in test_cases:
        result = string_rotation(s1, s2)
        print(f"string_rotation({s1!r}, {s2!r}) = {result} (expected: {expected}) → {'✅' if result == expected else '❌'}")