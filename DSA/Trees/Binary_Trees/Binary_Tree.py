class Binary_Tree_Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    @staticmethod
    def create_BTree_for_Test():
        root = Binary_Tree_Node("1")

        child1 = Binary_Tree_Node("2")
        child2 = Binary_Tree_Node("3")

        child21  = Binary_Tree_Node("21")
        child22  = Binary_Tree_Node("22")
        child31  = Binary_Tree_Node("31")
        child32  = Binary_Tree_Node("32")

        root.left = child1
        root.right = child2

        child1.left = child21
        child1.right = child22

        child2.left = child31
        child2.right = child32

        return root
    
    @staticmethod
    def print_BTree(root):
        if root == None:
            return
        print(root.data, end=": ")

        if root.left is None:
            print("L-> None", end=", ")
        else:
            print(f"L-> {root.left.data}", end=", ")
        
        if root.right is None:
            print("R-> None")
        else:
            print(f"R-> {root.right.data}")

        Binary_Tree_Node.print_BTree(root.left)
        Binary_Tree_Node.print_BTree(root.right)
    
    @staticmethod
    def take_Btree_input():
        data = int(input("Enter the vlaue of the new node: "))
        if data == -1:
            return
        node = Binary_Tree_Node(data)

        print(f"Enter left value for {data}")
        node.left = Binary_Tree_Node.take_Btree_input()
        print(f"Enter Right value for {data}")
        node.right = Binary_Tree_Node.take_Btree_input()

        return node