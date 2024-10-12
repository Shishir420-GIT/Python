# Stack is an abstract class, including method:  push, pop, isEmpty, size, peek/top
# This file is for create a Stack class using OOPS and list, byt restricting it's actions
class StackList:
    def __init__(self):
        self.__stack = [] # Keep this private
    
    def isEmpty(self):
        return len(self.__stack) == 0
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.__stack[-1]
    
    def push(self, n):
        self.__stack.append(n)

    def pop(self):
        if self.isEmpty():
            return None
        return self.__stack.pop()
    
    def size(self):
        return len(self.__stack)
    