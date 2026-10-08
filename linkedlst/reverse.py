class Node:
    def __init__(self, data):
        
        self.data=data
        self.next = None
        
        
head=Node(10)
head.next= Node(20)
head.next.next= Node(30)

def reverse(head):
    curr= head
    prev= None
    while curr:
        nxt=curr.next
        curr.next=prev
        prev=curr
        curr=nxt
        
    return prev
head = reverse(head)


curr=head
while curr:
    print(curr.data, end="->")
    curr= curr.next
    
print("None")
