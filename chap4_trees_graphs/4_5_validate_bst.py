import math

from chap4_trees_graphs.binary_search_tree import BinarySearchTree
from chap4_trees_graphs.binary_tree import BinaryTree


class BinaryNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


def validate_bst_recursive(node, more_then, less_then):
    if node is None:
        return True
    if not more_then < node.name < less_then:
        return False
    left = validate_bst_recursive(
        node.left, more_then, min(less_then, node.name)
    )
    right = validate_bst_recursive(
        node.right, max(more_then, node.name), less_then
    )
    return left and right


def validate_bst(node):
    """validate if a binary tree is a binary search tree."""
    return validate_bst_recursive(node, -math.inf, math.inf)


def is_binary_search_tree(tree):
    return _is_bst(tree.root)


def _is_bst(node, min_val=None, max_val=None):
    if not node:
        return True
    if (min_val and node.key < min_val) or (max_val and node.key >= max_val):
        return False
    return _is_bst(node.left, min_val, node.key) and _is_bst(
        node.right, node.key, max_val
    )


def test_is_binary_search_tree():
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)
    bst.insert(14)

    t = BinaryTree()
    n1 = t.insert(5, None)
    n2 = t.insert(4, n1)
    n3 = t.insert(6, n1)
    n4 = t.insert(3, n2)
    t.insert(6, n2)
    t.insert(5, n3)
    t.insert(2, n4)

    assert not is_binary_search_tree(t)
    assert is_binary_search_tree(bst)


if __name__ == "__main__":
    test_is_binary_search_tree()
