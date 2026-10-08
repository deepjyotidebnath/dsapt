class Node:
    def __init__(self, data):
        self.data= data
        self.left=None
        self.right=None
        
root= Node(1)
root.left= Node(3)
root.right = Node(5)
root.left.right=Node(9)
root.left.left=Node(9)

def count_leaf(node):
    if node is None:
        return
    if node.left is None and node.right is None:
        return 1
    return count_leaf(node.left) + count_leaf(node.right)

print(count_leaf(root))
        
        