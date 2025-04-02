def precedence(c):
    if c == '*':
        return 3
    elif c == '.':
        return 2
    elif c == '|':
        return 1
    else:
        return 0

def insert_concat_operators(regex):
    result = ""
    for i in range(len(regex)):
        curr = regex[i]
        result += curr

        if i + 1 < len(regex):
            next_char = regex[i + 1]

            curr_is_token = curr.isalnum() or curr in ['*', ')']
            next_is_token = next_char.isalnum() or next_char == '('

            if curr_is_token and next_is_token:
                result += '.'
    return result

def infix_to_postfix(expr):
    op_stack = []
    postfix = ""

    # Replace '+' with '|' for union
    expr = expr.replace('+', '|')

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
