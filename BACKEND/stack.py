#!/usr/bin/python3

#Python Project (Building a stack)

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is Empty")
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is Empty")
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
    
# INITIALIZE AN INSTANCE OF THE CLASS STACK
stack = Stack()

# APPEND ITEMS TO THE STACK 
stack.push(30)
stack.push(10)
stack.push(12)

# RETURN THE LAST ITEM FROM STACK 
print(stack.peek())
# OUTPUT : 12

# CHECK IF STACK IS EMPTY
print(stack.is_empty())
#OUTPUT: FALSE

# REMOVE LAST ITEM FROM STACK 
print(stack.pop())

#OUTPUT: 12

# RETURN LAST ITEM FROM STACK 
print(stack.peek())
#OUTPUT: 10

#RETURN THE SIZE OF THE STACK
print(stack.size())
# OUTPUT: 2
