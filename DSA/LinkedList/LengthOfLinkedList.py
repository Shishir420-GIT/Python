from Nodes import Nodes
import CreateLinkedList

# Methods are defined in Nodes.py file

head = CreateLinkedList.createForTest()

print(Nodes.lengthOfNodes(head))
print(Nodes.legnthOfNodesRecursively(Nodes, head))