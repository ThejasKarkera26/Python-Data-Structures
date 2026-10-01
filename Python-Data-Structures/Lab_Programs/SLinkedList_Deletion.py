# Creation of node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Creating LinkedList
class LinkedList:
    def __init__(self):
        self.head = None


    # Deletion at beginning
    def del_first_node(self):
        if self.head is None:
            print("No Element")
            return

        self.head = self.head.next


    # Deletion at end
    def del_at_end(self):
        if self.head is None:
            print("No Element")
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head

        while current.next.next is not None:
            current = current.next

        current.next = None


    # Deletion at given position
    def del_at_position(self, pos):
        if self.head is None:
            print("No Element")
            return

        if pos < 0:
            print("Invalid Position")
            return

        if pos == 0:
            self.del_first_node()
            return

        current = self.head
        count = 0

        # Traverse to the node before given position
        while current is not None and count < pos - 1:
            current = current.next
            count += 1

        if current is None or current.next is None:
            print("Position out of range")
            return

        current.next = current.next.next


    # Display the list
    def display(self):
        current = self.head
        elements = []

        while current:
            elements.append(str(current.data))
            current = current.next

        print("->".join(elements) if elements else "List is empty")


if __name__ == "__main__":
    lst = LinkedList()

    lst.head = Node(10)
    lst.head.next = Node(20)
    lst.head.next.next = Node(30)
    lst.head.next.next.next = Node(40)

    print("Original List:")
    lst.display()

    print("\nAfter deletion at beginning:")
    lst.del_first_node()
    lst.display()

    print("\nAfter deletion at end:")
    lst.del_at_end()
    lst.display()

    print("\nAfter deletion at position 1:")
    lst.del_at_position(1)
    lst.display()