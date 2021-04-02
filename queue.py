#fifo
"""
stock_price=[]
#everytime we should insert at 0 position
stock_price.insert(0,131.10)
stock_price.insert(0,132.12)
stock_price.insert(0,135)

print(stock_price)

print(stock_price.pop())


"""

from collections import deque

class Queue:
    def __init__(self):
        self.buffer=deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        self.buffer.pop()

    def is_empty(self):
        return len(self.buffer)==0

    def size(self):
        return len(self.buffer)

p=Queue()

p.enqueue(1)
p.enqueue(2)
p.enqueue(3)

print(p.buffer)
p.dequeue()
print(p.buffer)