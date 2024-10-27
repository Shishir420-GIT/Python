from Basic_Trees import TreeNode

root = TreeNode("CEO")

employee1 = TreeNode("Project Manager")
employee2 = TreeNode("Team Lead")
employee3 = TreeNode("Engineer")

root.children.append(employee1)
root.children.append(employee2)
root.children.append(employee3)

print(root.children)
print(root.data)
print(root.children[0].data)
print(root.children[1].data)
print(root.children[2].data)