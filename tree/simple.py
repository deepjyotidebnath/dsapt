class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create Tree
root = Node(10)

root.left = Node(20)
root.right = Node(30)

root.left.left = Node(40)
root.left.right = Node(50)

# Print Root
print(root.data)

def preorder(root):
    if root is None:
        return 
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)
print(preorder(root))

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)
print(inorder(root))

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")
print(postorder(root))