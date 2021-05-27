def binary_search(target, input_list):
    start_index = 0
    end_index = len(input_list) - 1

    while start_index <= end_index:
        middle_index = end_index + (start_index - end_index) // 2
        guess_value = input_list[middle_index]
        if guess_value == target:
            return True
        if guess_value > target:
            end_index = middle_index - 1
        else:
            start_index = middle_index + 1
    return False


list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(0, list))
