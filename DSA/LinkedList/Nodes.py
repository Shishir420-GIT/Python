class Nodes:
    def __init__(self, data):
        self.data = data
        self.nextData = None

    # Printing using Loops
    def printNodes(head):
        while head is not None:
            print(head.data, end=" ")
            head = head.nextData
        return None
    
    # Printing using Recursion
    def printNodesRecursively(self, head):
        if head is None:
            return
        print(head.data, end=" ")
        return self.printNodesRecursively(self, head.nextData)
    
    def lengthOfNodes(head):
        count = 0
        while head is not None:
            head = head.nextData
            count += 1
        return count
    
    def legnthOfNodesRecursively(self, head):
        if head is None:
            return 0
        return 1 + self.legnthOfNodesRecursively(self, head.nextData)