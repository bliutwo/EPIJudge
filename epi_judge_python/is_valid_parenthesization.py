from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    d = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for c in s:
        if c in d:
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            if d[stack[-1]] == c:
                stack.pop()
            else:
                return False
    return len(stack) == 0



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
