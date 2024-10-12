from OperationsInLinkedList import deleteAtHead, deleteAtTail, deleteAtTailRecursively, deleteAtIndex
from CreateLinkedList import createUsingLoop
from Nodes import Nodes

#Methods are defined in OperationInLinkedList.py fie.

head = createUsingLoop([22,33,44,55])
Nodes.printNodes(head)

# print("\n--------deleteAtHead---------\n")

# newHead = deleteAtHead(head) # head will remain same, add index
# Nodes.printNodes(newHead)

# print("\n--------deleteAtHead---------\n")

# newHead = deleteAtTail(newHead) # head will remain same, add index
# Nodes.printNodes(newHead)

# print("\n--------deleteAtTailRecursively---------\n")

# newHead = deleteAtTailRecursively(head) # head will remain same, add index
# Nodes.printNodes(newHead)

print("\n--------deleteAtIndex---------\n")

newHead = deleteAtIndex(head,0) # head will remain same, add index
Nodes.printNodes(newHead)