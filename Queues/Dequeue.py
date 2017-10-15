class Dequeue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


dq = Dequeue()

dq.addFront(1)

print(dq.size())

print(dq.removeFront())

dq.addFront("hello")
dq.addRear("World")

print(dq.removeFront() + ' ' + dq.removeRear())

print(dq.size())

print(dq.isEmpty())