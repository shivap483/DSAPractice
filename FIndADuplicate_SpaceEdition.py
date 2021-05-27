# O(n) time, O(n) space
def find_duplicate(input_list):
    numbers_set = set()
    for number in input_list:
        if number in numbers_set:
            return number
        numbers_set.add(number)
