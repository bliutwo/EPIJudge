from test_framework import generic_test


def evaluate(expression: str) -> int:
    stack = []
    l = expression.split(',')
    d = {'/': lambda y, x: x // y, '*': lambda y, x: x * y, '+': lambda y, x: x + y, '-': lambda y, x: x - y}
    for word in l:
        if word in d:
            stack.append(d[word](stack.pop(), stack.pop()))
        else:
            stack.append(int(word))
    return stack[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
