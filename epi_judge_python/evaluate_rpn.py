from test_framework import generic_test

def operation(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == 'x':
        return a * b
    elif operator == '/':
        return a // b
    else:
        raise ValueError

def evaluate(expression: str) -> int:
    s = expression.split(',')
    operands = ['+', '-', 'x', '/']
    curr_operator = None
    a = None
    b = None
    top = None
    while len(s) > 0:
        top = s.pop()
        if len(s) == 0:
            break
        if top in operands:
            curr_operator = top
        elif a == None and b == None:
            a = top
        elif a != None and b == None:
            b = top
        elif a and b and curr_operator:
            s.append(operation(a, b, curr_operator))
    return top


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
