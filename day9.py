class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def add_after(self, node):
        node.next = self.next
        node.prev = self
        self.next.prev = node
        self.next = node

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev


class Circular:
    def __init__(self, root):
        self.current = root
        self.score = {p: 0 for p in range(1, 419)}
        self.player = 2

    def add(self, marble):
        print(marble)
        if marble % 23 == 0:
            for _ in range(7):
                self.current = self.current.prev
            self.score[self.player] += marble
            self.score[self.player] += self.current.data
            self.current = self.current.next
            self.current.prev.remove()
        else:
            new_node = Node(marble)
            self.current.next.add_after(new_node)
            self.current = new_node

        self.player = (self.player % 418) + 1


zero = Node(0)
one = Node(1)
zero.next = one
zero.prev = one
one.prev = zero
one.next = zero

circular = Circular(one)
for i in range(2, 7133900):
    circular.add(i)
print(sorted(circular.score.items(), key=lambda x: x[1], reverse=True))
