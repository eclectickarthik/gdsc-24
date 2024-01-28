'''1) 	Problem Statement:
You are given a string containing three types of parentheses: '(', ')', '{', '}', '[' and ']'. The goal is to determine whether the input string is valid or not.'''

def is_valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False
        else:
            return False

    return not stack

# Test cases
print(is_valid_parentheses("()"))  # True
print(is_valid_parentheses("(]"))  # False