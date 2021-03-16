from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import collections


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    bfs_q = collections.deque([tree])
    curr_level = collections.deque([tree.data])
    ans = []
    while len(bfs_q) != 0:
        curr = bfs_q.popleft()
        if curr != None:
            bfs_q.append(curr.left)
            bfs_q.append(curr.right)
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
