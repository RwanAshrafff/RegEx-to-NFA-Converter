
import re

def validate_regex(expr):
    # Allow only: a-z A-Z 0-9 | * + ? ( ) and whitespace
    pattern = r"^[a-zA-Z0-9|*+?.() ]*$"
    if not re.fullmatch(pattern, expr):
        raise ValueError("❌ Invalid characters in regex. Allowed: a-z, A-Z, 0-9, |, *, +, ?, ., (, )")
    
def precedence(c):
    if c in ['*', '+', '?']:
        return 4
    elif c == '.':
        return 3
    elif c == '|':
        return 2
    else:
        return 0

def insert_concat_operators(regex):
    result = ""
    for i in range(len(regex)):
        curr = regex[i]
        result += curr

        if i + 1 < len(regex):
            next_char = regex[i + 1]

            # Characters that imply end of one operand
            curr_is_end = curr.isalnum() or curr in ['*', '+', '?', ')']
            # Characters that imply start of next operand
            next_is_start = next_char.isalnum() or next_char == '('

            if curr_is_end and next_is_start:
                result += '.'
    return result

def infix_to_postfix(expr):
    validate_regex(expr)
    op_stack = []
    postfix = ""

    for c in expr:
        if c == ' ':
            continue
        elif c.isalnum():
            postfix += c + ' '
        elif c == '(':
            op_stack.append(c)
        elif c == ')':
            while op_stack and op_stack[-1] != '(':
                postfix += op_stack.pop() + ' '
            if op_stack: op_stack.pop()  # remove '('
        else:
            while op_stack and precedence(c) <= precedence(op_stack[-1]):
                postfix += op_stack.pop() + ' '
            op_stack.append(c)

    while op_stack:
        postfix += op_stack.pop() + ' '

    return postfix.strip()
