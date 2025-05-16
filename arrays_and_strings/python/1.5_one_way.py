def one_away(s1: str, s2: str) -> bool:
    # Early exit for length gap
    if abs(len(s1) - len(s2)) > 1:
        return False

    # Assign shorter and longer
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    i = j = 0
    found_difference = False

    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if found_difference:
                return False
            found_difference = True

            if len(s1) == len(s2):
                i += 1  # Move both if same length (replace case)
        else:
            i += 1  # Move shorter if same

        j += 1  # Always move longer

    return True