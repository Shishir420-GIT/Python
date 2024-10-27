from Binary_Tree import Binary_Tree_Node

def take_Btree_input():
    data = int(input("Enter the vlaue of the new node: "))
    if data == -1:
        return
    node = Binary_Tree_Node(data)

    print(f"Enter left value for {data}")
    node.left = take_Btree_input()
    print(f"Enter Right value for {data}")
    node.right = take_Btree_input()

    return node

# root = take_Btree_input()
# Binary_Tree_Node.print_BTree(root)

def take_Btree_input_level():
    
    pass