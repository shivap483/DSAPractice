def get_closing_paren(input_string, opening_paren_index):
    open_nested_paren = 0
    for position in range(opening_paren_index + 1, len(input_string)):
        char = input_string[position]
        if char is ")" and open_nested_paren is 0:
            return position
        if char is "(":
            open_nested_paren += 1
        if char is ")":
            open_nested_paren -= 1
    raise Exception("No closing parenthesis")
