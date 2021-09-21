class Node:

    def __init__(self, value):
        self.value = value
        self.above = None
        self.below = None


class Stack:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.top = None
        self.bottom = None

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def join(self, above, below):
        if below:
            below.above = above
        if above:
            above.below = below

    def push(self, value):
        if self.size >= self.capacity:
            return False
        self.size += 1
        node = Node(value)
        if self.size == 1:
            self.bottom = node
        self.join(node, self.top)
        self.top = node
        return True
    