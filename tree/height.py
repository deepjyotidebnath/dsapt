class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
        
root=Node(10)
root.left = Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)

def height(node):
    if node is None:
        return 0
    left_height = height(node.left)
    right_height=height(node.right)
    
    return 1+max(left_height, right_height)

print("HEIGHT", height(root))