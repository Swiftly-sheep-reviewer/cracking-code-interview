from chap2_linked_list.linked_list import *


def delete_middle_node(node):
    """
    Input: the node c from a -> b -> c -> d -> e -> f
    Result: a -> b -> d -> e -> f
    """
    node.value = node.next.value
    node.next = node.next.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.add_multiple([1, 2, 3, 4])
    middle_node = ll.add(5)
    ll.add_multiple([7, 8, 9])

    print(ll)
    delete_middle_node(middle_node)
    print(ll)
