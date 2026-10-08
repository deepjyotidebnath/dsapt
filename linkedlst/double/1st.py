class Node:
    def __init__(self, data):
        self.data= data
        self.prev=None
        self.next=None
first = Node(10)
second=Node(20)
third= Node(30)

first.next=second
second.prev=first

second.next=third
third.prev=second

current = first
while current:
    print(current.data, end="<->")
    current=current.next
print("None")