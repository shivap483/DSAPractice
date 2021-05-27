import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(input_list):
    if len(input_list) <= 1:
        return input_list
    last_index = len(input_list) - 1

    for index_we_are_choosing_for in range(0, last_index):

        random_choice_index = get_random(0, last_index)

        if random_choice_index != index_we_are_choosing_for:
            input_list[index_we_are_choosing_for], input_list[random_choice_index] = \
                input_list[random_choice_index], input_list[index_we_are_choosing_for]

    return input_list


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(list)
shuffle(list)
print(list)
