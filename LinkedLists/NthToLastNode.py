class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None

def nth_to_last_node(head, num):

    temp = head
    count = 0
    while (temp):
        count += 1
        temp = temp.nextnode
    pos = count - num + 1
    c = 1
    while (head):
        if c == pos:
            return (head.value)
        head = head.nextnode
        c += 1

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e
e.nextnode = f
f.nextnode = g
g.nextnode = h

target_node = nth_to_last_node(a, 2)
print(target_node)