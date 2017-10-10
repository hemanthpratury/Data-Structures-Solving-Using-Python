class Node(object):

    def __init__(self,value):

        self.value = value
        self.nextnode = None

def reverse(node):

    prev_node = None
    next_node = None
    current_node = node

    while (current_node != None):

        next_node = current_node.nextnode

        current_node.nextnode = prev_node

        prev_node = current_node
        current_node = next_node

    return prev_node

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e


print(a.value)
print(a.nextnode.value)
print(c.value)
print(c.nextnode.value)
#print(e.nextnode.value)

head = reverse(a)

print()
while head:
    print(head.value)
    head = head.nextnode



