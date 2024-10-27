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
    