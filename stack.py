#list are not effective in stacks because of unwanted memory allocation so collections deque were used instead

"""from collections import deque
s=deque()
s.append("one")
s.append("two")
s.append("three")
print(s)
"""
from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)


def reverse(string):
    stack=Stack()
    
    for r in string:
        stack.push(r)
    rev=''
    while stack.size()!=0:
        rev+=stack.pop()
    return rev 


if __name__ == '__main__':
    print(reverse("We will conquere COVI-19"))
    print(reverse("I am the king"))
