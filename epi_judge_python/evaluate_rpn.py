from test_framework import generic_test


def evaluate(expression: str) -> int:
    l = expression.split(',')
    stack = []
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
