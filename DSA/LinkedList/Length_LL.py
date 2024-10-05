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

def count_LL(head):
    count = 0
    while head is not None:
        count += 1
        head = head.nextPage
    return count

def count_LL_R(head):
    if head is None:
        return 0
    return 1 + count_LL_R(head.nextPage)

print(count_LL(head))
print(count_LL_R(head))

