class Nodes:
    def __init__(self, page):
        self.page = page
        self.nextPage = None

def print_LL_Loop(head):
    while head is not None:
        print(head.page, end="->")
        head = head.nextPage
    return

def takeLLInput():
    value= input("Enter Value: ")
    head = None
    previousNode = None
    while value != "-1":
        new_node = Nodes(value)
        if head is None:
            head = new_node
        else:
            last = head
            while last.nextPage is not None:
                last = last.nextPage
            last.nextPage = new_node
        value= input("Enter Value: ")
    return head

def takeLLInputOptimized():
    value= input("Enter Value: ")
    head = None
    previousNode = None
    while value != "-1":
        new_node = Nodes(value)
        if head is None:
            head = new_node
            previousNode = new_node
        else:
            previousNode.nextPage = new_node
            previousNode = new_node
        value= input("Enter Value: ")
    return head

#head = takeLLInput()
head = takeLLInputOptimized()
print_LL_Loop(head)

