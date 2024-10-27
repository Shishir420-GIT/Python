from Trees import TreeNode
from collections import deque


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

root = take_input_in_level()
TreeNode.print_tree_detailed(root)