from Binary_Tree import Binary_Tree_Node


# Creating a Binary Tree
root = Binary_Tree_Node("1")

child1 = Binary_Tree_Node("2")
child2 = Binary_Tree_Node("3")

root.left = child1
root.right = child2

# Printing a binary tree
print(root.data)
print(root.left)
print(root.left.data)
print(root.right)
print(root.right.data)