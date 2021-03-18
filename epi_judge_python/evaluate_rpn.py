from test_framework import generic_test


def evaluate(expression: str) -> int:
    l = expression.split(',')
    d = {'*': lambda y, x: x * y, '/': lambda y, x: x // y, '+': lambda y, x: x + y, '-': lambda y, x: x - y}
    stack = []
    for elem in l:
        if elem in d:
            stack.append(d[elem](int(stack.pop()), int(stack.pop())))
        else:
            stack.append(int(elem))
    return stack[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
