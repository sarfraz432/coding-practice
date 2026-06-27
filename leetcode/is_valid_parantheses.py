
def is_valid(para_str:str) -> bool:
    braces_stack = []
    top = -1
    try:
        for cur_char in para_str:
            if cur_char in [']', '}', ')']:
                if top > -1:
                    last_brace = braces_stack.pop(top)
                    if last_brace == '(' and cur_char == ')' or\
                    last_brace == '[' and cur_char == ']'or\
                    last_brace == '{' and cur_char == '}':
                        top -= 1
                    else:
                        return False
            elif cur_char in ['[', '{', '(']:
                braces_stack.append(cur_char)
                top += 1
    except IndexError:
        return False
    if top == -1:
        return True
    else:
        return False
                

print(is_valid("()"))      # Expected: True
print(is_valid("()[]{}"))  # Expected: True
print(is_valid("(]"))      # Expected: False
print(is_valid("([)]"))    # Expected: False
print(is_valid("{[]}"))    # Expected: True
print(is_valid("(()"))    # Expected: False