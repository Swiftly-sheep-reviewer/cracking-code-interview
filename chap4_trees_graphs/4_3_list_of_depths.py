from collections import deque

from chap2_linked_list.linked_list import *


class BinaryNode:

    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def create_node_list_by_depth(tree_root):
    # BFS
    levels = {}
    queue = deque()
    queue.append((tree_root, 0))

    while len(queue) > 0:
        node, level = queue.popleft()
        if level not in levels:
            # First node in that level
            levels[level] = LinkedList()
        # Nodes already exist, add node to linked list
        levels[level].add(node)

        # Push onto queue
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    return levels


def create_node_list_by_depth_b(tree):
    if not tree:
        return []

    current = tree
    result = [LinkedList([current])]
    level = 0

    while result[level]:
        result.append(LinkedList())
        for linked_list_node in result[level]:
            tree_node = linked_list_node.value
            if tree_node.left:
                result[level + 1].add(tree_node.left)
            if tree_node.right:
                result[level + 1].add(tree_node.right)
        level += 1
    return result


testable_functions = [create_node_list_by_depth, create_node_list_by_depth_b]


def test_create_node_list_by_depth():
    for f in testable_functions:
        node_h = BinaryNode("H")
        node_g = BinaryNode("G")
        node_f = BinaryNode("F")
        node_e = BinaryNode("E", node_g)
        node_d = BinaryNode("D", node_h)
        node_c = BinaryNode("C", None, node_f)
        node_b = BinaryNode("B", node_d, node_e)
        node_a = BinaryNode("A", node_b, node_c)
        lists = f(node_a)

        assert lists[0].values() == LinkedList([node_a]).values()
        assert lists[1].values() == LinkedList([node_b, node_c]).values()
        assert lists[2].values() == LinkedList(
            [node_d, node_e, node_f]).values()
        assert lists[3].values() == LinkedList([node_h, node_g]).values()


def example():
    root = BinaryNode(0)
    root.left = BinaryNode(1)
    root.right = BinaryNode(2)
    root.left.left = BinaryNode(3)
    root.left.right = BinaryNode(4)
    root.right.left = BinaryNode(5)
    root.right.right = BinaryNode(6)

    levels = create_node_list_by_depth(root)
    print(levels)


if __name__ == "__main__":
    example()
