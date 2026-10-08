class Node:
    def __init__(self, data):
        self.data= data
        self.next= None  
        
def count(head):
    if head is None:
        return 0
    count =1
    current = head.next
    
    while current != head:
        count += 1
        current = current.next 
    return count

head = Node(20)
first= Node(30)
second= Node(40)
third= Node(50)

head.next=first
first.next = second
second.next = third 
third.next = head


print("COUNT", count(head))