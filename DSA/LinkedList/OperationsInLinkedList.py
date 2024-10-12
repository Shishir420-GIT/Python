from Nodes import Nodes
from CreateLinkedList import createUsingLoop

def insertAtHead(head, value):
    newNode = Nodes(value)
    newNode.nextData = head
    head = newNode
    return head

def insertAtTail(head, value):
    newNode = Nodes(value)
    if head is None:
        return newNode
    tail = head
    while tail.nextData is not None:
        tail = tail.nextData
    tail.nextData = newNode

def insertAtTailRecursive(head, value): 
    if head is None:
        newNode = Nodes(value)
        return newNode
    head.nextData = insertAtTailRecursive(head.nextData, value)
    return head

def insertAtIndex(head,index,value):
    newNode = Nodes(value)
    if index == 0: # insert at tail
        return insertAtHead(head, value)

    if index == Nodes.lengthOfNodes(head): # insert at tail
        insertAtTail(head,value)
        return head
    
    newNode.nextData = head
    tail = head
    indexValue = 0
    while tail is not None and indexValue < index - 1:
        tail = tail.nextData
        indexValue += 1
    if tail is None:
        print("Index out fo Range")
        return head
    newNode.nextData = tail.nextData
    tail.nextData = newNode
    return head

def insertAtIndexRecursive(head,index,value):
    newNode = Nodes(value)
    if index == 0: # insert at tail
        return insertAtHead(head, value)
    head.nextData = insertAtIndexRecursive(head.nextData,index-1,value)

    return head

def deleteAtHead(head):
    if head is None:
        return head
    head = head.nextData
    return head

def deleteAtTail(head):
    if head is None:
        return head
    tail = head
    while tail.nextData.nextData is not None:
        tail = tail.nextData
    tail.nextData = None
    return head

def deleteAtTailRecursively(head):
    if head is None or head.nextData is None:
        return None
    head.nextData = deleteAtTail(head.nextData)
    return head

def deleteAtIndex(head, index):
    if index == 0:
        head = head.nextData
        return head
    tail = head
    indexValue = 0
    while tail.nextData is not None and indexValue < index -1:
        print(indexValue,index,index-1, indexValue < index -1)
        tail = tail.nextData
        indexValue += 1
    if tail.nextData is None:
        print("Index out of range")
        return head
    tail.nextData = tail.nextData.nextData
    return head