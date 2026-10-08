class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def delete(self, value):
        # Empty list
        if self.head is None:
            return

        # Delete first node
        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head

        # Find the node to delete
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return

            current = current.next

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


ll = LinkedList()

ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)
ll.head.next.next.next = Node(40)

ll.display()

ll.delete(30)

ll.display()
