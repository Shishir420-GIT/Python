import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from LinkedList.Nodes import Nodes

class LinkedListStack:
    def __init__(self,page):
        self.newNode = Nodes(page)
        print(self.newNode.page)
        print(self.newNode.nextPage)
    def isEmpty(self):
        return self.newNode is None
    
    def peek(self):
        return self.newNode.page
    
print(LinkedListStack(20))