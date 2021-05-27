def get_max_product_of_3(list_of_ints):
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])
    lowest_product_of_2 = highest_product_of_2 = highest * lowest
    highest_product_of_3 = highest_product_of_2 * list_of_ints[2]

    for current_index in range(2, len(list_of_ints)):
        current_number = list_of_ints[current_index]
        highest_product_of_3 = max(highest_product_of_3, highest_product_of_2 * current_number,
                                   lowest_product_of_2 * current_number)
        potential_highest = highest * current_number
        potential_lowest = lowest * current_number
        highest_product_of_2 = max(highest_product_of_2, potential_highest, potential_lowest)
        lowest_product_of_2 = min(lowest_product_of_2, potential_lowest, potential_highest)
        highest = max(highest, current_number)
        lowest = min(lowest, current_number)
    return highest_product_of_3


ints = [-10, -10, 1, 3, 2]
ints_ = [1, 10, -5, 1, -100]
print(get_max_product_of_3(ints_))
