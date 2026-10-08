class Node:
    def __init__(self, data):
        self.data= data
        self.right= None
        self.left = None
def pathsum(root, targetsum):
    if root is None:
        return False
    if root.left is None and root.right is None:
        return targetsum==root.data
    
    return (
        pathsum(root.left, targetsum-root.data)
        or
        pathsum(root.right, targetsum - root.data))
    
root = Node(5)
root.left=Node(4)
root.right = Node(8)

root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right=Node(4)

print(pathsum(root, 22))
    