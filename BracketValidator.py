def validate_brackets(in_string):
    openers_to_closers = {
        "[": "]", "{": "}", "(": ")"
    }
    openers = set(openers_to_closers.keys())
    closers = set(openers_to_closers.values())
    openers_stack = []
    for char in in_string:
        if char in openers:
            openers_stack.append(char)
        elif char is closers:
            if not openers_stack:
                return False
            else:
                last_unclosed_opener = openers_stack.pop()
                if not openers_to_closers[last_unclosed_opener] == char:
                    False
    return openers_stack == []
