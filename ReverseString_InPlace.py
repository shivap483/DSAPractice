def reverse(list):
    end = len(list) - 1
    start = 0
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1
    return list


string = "sDKJCNd"
print(string)
string = reverse(list(string))
print("".join(string))
