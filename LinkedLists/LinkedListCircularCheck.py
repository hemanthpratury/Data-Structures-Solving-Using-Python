class Node(object):

    def __init__(self,value):

        self.value = value
        self.nextnode = None



def cyclecheck(node):

    marker1 = node
    marker2 = node

    while marker2 != None and marker2.nextnode != None:

        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        if marker1 == marker2:
            return True
    return False


# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z

test1 = cyclecheck(a)
print(test1)

test2 = cyclecheck(x)
print(test2)


