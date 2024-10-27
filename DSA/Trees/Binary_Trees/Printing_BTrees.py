from Binary_Tree import Binary_Tree_Node

root = Binary_Tree_Node.create_BTree_for_Test()
# print(root.data)
# print(root.left)
# print(root.left.data)
# print(root.right)
# print(root.right.data)

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
    print_BTree(root.left)
    print_BTree(root.right)

Binary_Tree_Node.print_BTree(root)