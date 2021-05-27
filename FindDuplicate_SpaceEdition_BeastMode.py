def find_duplicate(list_items):
    n = len(list_items) - 1

    position_in_cycle = n + 1
    for _ in range(n):
        position_in_cycle = list_items[position_in_cycle - 1]

    remembered_position_in_cycle = position_in_cycle
    current_position_in_cycle = list_items[position_in_cycle - 1]
    cycle_step_count = 1
    while remembered_position_in_cycle is not current_position_in_cycle:
        current_position_in_cycle = list_items[current_position_in_cycle - 1]
        cycle_step_count += 1

    first_pointer = n + 1
    second_pointer = n + 1
    for _ in range(cycle_step_count):
        second_pointer = list_items[second_pointer - 1]

    while first_pointer is not second_pointer:
        first_pointer = list_items[first_pointer - 1]
        second_pointer = list_items[second_pointer - 1]
    return first_pointer


int = [4, 4, 6, 5, 2, 3, 1]
print(find_duplicate(int))
