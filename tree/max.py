class Node:
    def __init__(self, data):
        self.data= data
        self.left=None
        self.right=None
root=Node(10)
root.left=Node(20)
root.right= Node(30)

def find_max(node):
    if node is None:
        return float('-inf')
    return max(node.data, find_max(node.left),find_max(node.right) )

print(find_max(root))
        