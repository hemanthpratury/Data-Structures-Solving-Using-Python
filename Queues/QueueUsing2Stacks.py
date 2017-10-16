class Queue2Stacks(object):

    def __init__(self):

        self.stack1 = []
        self.stack2 = []

    def enqueue(self,item):

        self.stack1.append(item)


    def dequeue(self):

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()


Q2S = Queue2Stacks()
Q2S.enqueue(1)
Q2S.enqueue(2)
Q2S.enqueue(3)
print(Q2S.dequeue())
Q2S.enqueue(4)
print(Q2S.dequeue())
print(Q2S.dequeue())
print(Q2S.dequeue())
