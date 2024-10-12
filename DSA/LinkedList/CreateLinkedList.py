from Nodes import Nodes # Import Nodes class, for creating and printing Nodes

# Basic way

def createForTest():
    firstNode = Nodes(10)
    secondNode = Nodes(20)
    thirdNode = Nodes(30)
    fourthNode = Nodes(40)
    fifthNode = Nodes(50)

    head=firstNode
    firstNode.nextData = secondNode
    secondNode.nextData = thirdNode
    thirdNode.nextData = fourthNode
    fourthNode.nextData = fifthNode
    return head


def createUsingLoop(data_to_add):
    """
    # Using Loop
    # We used a list here, Same can be used to take input from a user
    """
    #data_to_add = [11,22,33,44,55]
    head = None
    previousNode = None
    for data in data_to_add:
        new_node = Nodes(data)
        if head == None:
            head = new_node
            previousNode = new_node
        else:
            previousNode.nextData = new_node
            previousNode = new_node
            del new_node
    return head

def createUsingUserInput():
    """
    # Taking input from a user
    """
    #data_to_add = [11,22,33,44,55]
    head = None
    previousNode = None
    data = 0
    while data != -1:
        data = int(input("Enter the next number: "))
        if data == -1:
            break
        new_node = Nodes(data)
        if head == None:
            head = new_node
            previousNode = new_node
        else:
            previousNode.nextData = new_node
            previousNode = new_node
            del new_node
    return head
