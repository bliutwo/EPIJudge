from test_framework import generic_test
from test_framework.test_failure import TestFailure
import collections


class Queue:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.l = []
        self.start = 0
        self.end = 0
        return

    def enqueue(self, x: int) -> None:
        self.l.append(x)
        self.end += 1
        return

    def dequeue(self) -> int:
        orig_start = self.start
        self.start += 1
        return self.l[orig_start]

    def size(self) -> int:
        return self.end - self.start


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
