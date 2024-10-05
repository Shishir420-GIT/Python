class Nodes:
    def __init__(self, page):
        self.page = page
        self.nextPage = None


first = Nodes(1)
second = Nodes(2)
third = Nodes(3)
fourth = Nodes(4)

first.nextPage = second
second.nextPage = third
third.nextPage = fourth
fourth.nextPage = None

head = first

def print_LL_Loop(head):
    while head is not None:
        print(head.page, end=" ")
        head = head.nextPage
    return

def print_LL_R(head):
    if head is None:
        return
    print(head.page, end=" ")
    return print_LL_R(head.nextPage)

print_LL_Loop(head)
print()
print_LL_R(head)