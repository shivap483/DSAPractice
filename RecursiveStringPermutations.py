def get_permutation(string):
    if len(string) <= 1:
        return set([string])

    all_chars_except_last = string[:-1]
    last_char = string[-1]
    permutations_of_all_chars_except_last = get_permutation(all_chars_except_last)

    permutations = set()
    for string in permutations_of_all_chars_except_last:
        for position in range(len(all_chars_except_last)):
            permutation = (string[:position] + last_char + string[position:])
            permutations.add(permutation)

    return permutations


temp = get_permutation("cats")
print(temp)
print(len(temp))
