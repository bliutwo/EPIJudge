from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    ans = []
    if not tree:
        return ans
    curr_level = [tree]
    while curr_level:
        ans.append([node.data for node in curr_level])
        curr_level = [child for node in curr_level for child in (node.left, node.right) if child]
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
