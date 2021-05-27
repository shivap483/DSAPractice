def find_rotation_point(input_list):
    start_index = 0
    end_index = len(input_list) - 1
    if input_list[start_index] < input_list[end_index]:
        return start_index

    while start_index <= end_index:
        middle_index = start_index + (end_index - start_index) // 2
        potential_rotation_point = input_list[middle_index]
        before_rotation_point = input_list[middle_index - 1]
        last_element = input_list[end_index]

        if before_rotation_point > potential_rotation_point:
            return middle_index
        elif potential_rotation_point > last_element:
            start_index = middle_index + 1
        else:
            end_index = middle_index - 1
    return False


words = ['v', 'a', 'b', 'c', 'k']
print(find_rotation_point(words))
