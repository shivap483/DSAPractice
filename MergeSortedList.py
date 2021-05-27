def merge_remaining(leftover, index, merged_list, cur_index):
    while index < len(leftover):
        merged_list[cur_index] = leftover[index]
        index += 1


def merge(left, right):
    left_i = 0
    right_i = 0
    cur_index = 0
    while left_i < len(left) and right_i < len(right):
        if left[left_i] < right[right_i]:
            merged_list[cur_index] = left[left_i]
            left_i += 1
        else:
            merged_list[cur_index] = right[right_i]
            right_i += 1
        cur_index += 1

    if left_i < len(left):
        merge_remaining(left, left_i, merged_list, cur_index)

    if right_i < len(right):
        merge_remaining(right, right_i, merged_list, cur_index)


left_array = [3, 4, 6, 10, 11, 15]
right_array = [1, 5, 8, 12, 14, 19]
merged_list = [None] * (len(left_array) + len(right_array))
merge(left_array, right_array)
print(merged_list)
