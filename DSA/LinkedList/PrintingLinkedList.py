import Nodes
import CreateLinkedList

# Methods are defined in Nodes.py file

head = CreateLinkedList.createForTest()
print(head)
Nodes.Nodes.printNodes(head)

head = CreateLinkedList.createUsingLoop([11,22,33,44,55])
print(head)
Nodes.Nodes.printNodes(head)

head = CreateLinkedList.createUsingUserInput()
print(head)
Nodes.Nodes.printNodes(head)
