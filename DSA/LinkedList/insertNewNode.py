from OperationsInLinkedList import insertAtHead, insertAtTail, insertAtTailRecursive, insertAtIndex
from CreateLinkedList import createUsingLoop
from Nodes import Nodes

#Methods are defined in OperationInLinkedList.py fie.

head = createUsingLoop([22,33,44,55])
value = 11

print("\n--------insertAtHead---------\n")
newHead = insertAtHead(head, value)
Nodes.printNodes(newHead)

print("\n--------insertAtTail---------\n")

insertAtTail(newHead, value) # head will remain the same
Nodes.printNodes(newHead)

print("\n--------insertAtTailRecursive---------\n")

insertAtTailRecursive(newHead, value) # head will remain the same
Nodes.printNodes(newHead)

print("\n--------insertAtIndex---------\n")

newHead = insertAtIndex(newHead,0,90) # head will remain same, add index
Nodes.printNodes(newHead)

print("\n--------insertAtIndexRecursive---------\n")

newHead = insertAtIndex(newHead,0,100) # head will remain same, add index
Nodes.printNodes(newHead)