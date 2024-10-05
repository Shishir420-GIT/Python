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

print(head)
