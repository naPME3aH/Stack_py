def is_valid_string(s):
    stack = []
    for ch in s:
        if ch in ['[', '{', '(']:
            stack.append(ch)
        elif ch == ']':
            if not stack or stack[-1] != '[':
                return "Bruh"
            stack.pop()
        elif ch == '}':
            if not stack or stack[-1] != '{':
                return "Bruh"
            stack.pop()
        elif ch == ')':
            if not stack or stack[-1] != '(':
                return "Bruh"
            stack.pop()
    if stack:
        return "Bruh"
    return "Nice"

s = '([{}]())'
print(is_valid_string(s))
