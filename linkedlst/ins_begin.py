class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_begin(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node


def print_list(head):
    temp = head

    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next

    print("None")


# Create Linked List
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Before:")
print_list(head)

# Insert 5 at beginning
head = insert_begin(head, 5)

print("After:")
print_list(head)