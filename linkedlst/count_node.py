class Node:
    def __init__(self, data):
        self.data= data
        self.next = None
a=Node(10)
a.next=Node(20)
a.next.next=Node(30)
a.next.next.next=Node(40)

def count_node(head):
    count = 0
    current = head
    while current is not None:
        count +=1
        current = current.next 
    return count
    
print(count_node(a))