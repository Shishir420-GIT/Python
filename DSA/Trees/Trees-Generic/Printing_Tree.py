from Trees import TreeNode

def print_tree(root):
    print(root.data)
    for node in root.children:
        print_tree(node)

root = TreeNode.create_Tree_for_Test()
print_tree(root)

def print_tree_detailed(root):
    if root == None:
        return
    print(root.data,end=":")
    for node in root.children:
        print(node.data, end=",")
    print()
    for node in root.children:
        print_tree_detailed(node)

print_tree_detailed(root)