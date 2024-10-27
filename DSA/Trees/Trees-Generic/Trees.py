from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def create_Tree_for_Test():
        root = TreeNode("1")

        child1 = TreeNode("2")
        child2 = TreeNode("3")
        child3 = TreeNode("4")

        root.children.append(child1)
        child1.children.append(child2)
        root.children.append(child3)
        return root
    
    def print_tree(self, root):
        print(root.data)
        for node in root.children:
            self.print_tree(node)

    def print_tree_detailed(self, root):
        if root == None:
            return
        print(root.data,end=":")
        for node in root.children:
            print(node.data, end=",")
        print()
        for node in root.children:
            self.print_tree_detailed(node)

    def take_input_in_level():
        root_node = input("Enter the Root Node: ")
        root = TreeNode(root_node)

        queue = deque([root])

        while len(queue) != 0:
            current_node = queue.popleft()
            children_nodes = int(input(f"Enter the number of children for {current_node.data}: "))

            for _ in range(children_nodes):
                children_node = input(f"Enter the data for {_+1} children of {current_node.data}: ")
                new_node = TreeNode(children_node)
                current_node.children.append(new_node)
                queue.append(new_node)
        return root