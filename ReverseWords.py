def reverse_words(sentence):
    reverse_char(sentence, 0, len(message) - 1)
    start = 0
    length = len(sentence)
    for end in range(length + 1):
        if end == length or sentence[end] == " ":
            reverse_char(sentence, start, end - 1)
            start = end + 1


def reverse_char(chars, start, end):
    while start < end:
        chars[start], chars[end] = chars[end], chars[start]
        start += 1
        end -= 1


message = ['c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l']
print(message)
reverse_words(message)
print("".join(message))
