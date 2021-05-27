def has_palindrome_permutation(input_array):
    unpaired_characters = set()
    for char in input_array:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)
    if len(unpaired_characters) <= 1:
        return True
    return False


def is_string_palindrome(string):
    length_of_string = len(string)
    if length_of_string == 0:
        return True
    start = 0;
    end = length_of_string - 1
    while start is not end:
        if string[start] is not string[end]:
            return False
        start += 1
        end -= 1

    return True


print(has_palindrome_permutation(list("ivicc")))
