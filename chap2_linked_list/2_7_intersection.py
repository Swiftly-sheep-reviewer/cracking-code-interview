from chap2_linked_list.linked_list import *


def intersection(list1: LinkedList, list2: LinkedList):
    """
    Check if 2 lists have intersection, if there is one, all nodes will be the
    same starting from the intersect node.

    Args:
        list1: LinkedList 1
        list2: LinkedList 2
    Returns:
        True if 2 lists intersect, False otherwise.
    """
    if list1.tail is not list2.tail:
        return False

    shorter = list1 if len(list1) < len(list2) else list2
    longer = list2 if len(list1) < len(list2) else list1

    diff = len(longer) - len(shorter)

    shorter_node, longer_node = shorter.head, longer.head

    for _ in range(diff):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node


def test_linked_list_intersection():
    shared = LinkedList()
    shared.add_multiple([1, 2, 3, 4])

    a = LinkedList([10, 11, 12, 13, 14, 15])
    b = LinkedList([20, 21, 22])

    a.tail.next = shared.head
    a.tail = shared.tail
    b.tail.next = shared.head
    b.tail = shared.tail

    # should be 1
    print(intersection(a, b).value)
    assert intersection(a, b).value == 1


if __name__ == "__main__":
    test_linked_list_intersection()
