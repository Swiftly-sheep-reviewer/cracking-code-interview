from chap3_stacks_queues.stack import Stack


class MinStack(Stack):

    def __init__(self):
        super(MinStack, self).__init__()
        self.min_values = Stack()

    def push(self, value):
        super(MinStack, self).push(value)
        if not self.min_values or value <= self.minimum():
            self.min_values.push(value)

    def pop(self):
        value = super(MinStack, self).pop()
        if value == self.minimum():
            self.min_values.pop()
        return value

    def minimum(self):
        return self.min_values.peek()


def test_min_stack():
    new_stack = MinStack()
    assert new_stack.minimum() is None

    new_stack.push(5)
    assert new_stack.minimum() == 5

    new_stack.push(6)
    assert new_stack.minimum() == 5

    new_stack.push(3)
    assert new_stack.minimum() == 3

    new_stack.push(7)
    assert new_stack.minimum() == 3

    new_stack.push(3)
    assert new_stack.minimum() == 3

    new_stack.pop()
    assert new_stack.minimum() == 3

    new_stack.pop()
    assert new_stack.minimum() == 3

    new_stack.pop()
    assert new_stack.minimum() == 3

    new_stack.push(1)
    assert new_stack.minimum() == 1


if __name__ == "__main__":
    test_min_stack()
