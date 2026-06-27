
def is_valid(para_str:str) -> bool:
    return is_valid_optimized(para_str)
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
    

def is_valid_optimized(para_str:str) -> bool:
    mapping = {")": "(", "}": "{", "]": "["}
    stack = []
    for cur_char in para_str:
        if cur_char in mapping:
            top_element = stack.pop() if stack else "S"
            if mapping[cur_char] != top_element:
                return False
        else:
            stack.append(cur_char)
    return len(stack) == 0

                

print(is_valid("()"))      # Expected: True
print(is_valid("()[]{}"))  # Expected: True
print(is_valid("(]"))      # Expected: False
print(is_valid("([)]"))    # Expected: False
print(is_valid("{[]}"))    # Expected: True
print(is_valid("(()"))    # Expected: False