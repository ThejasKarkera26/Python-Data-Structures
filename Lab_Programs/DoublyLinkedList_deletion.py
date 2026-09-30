class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None


    # Insert at beginning
    def insert_at_begin(self, data):
        new_node = Node(data)

        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node

        self.head = new_node


    # Deletion at beginning
    def del_first_node(self):
        temp = self.head

        if self.head is None:
            print("No element")
            return

        self.head = temp.next

        if self.head is not None:
            self.head.prev = None


    # Deletion at end
    def del_at_end(self):
        if self.head is None:
            print("No element")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.prev.next = None


    # Deletion at given position
    def del_at_position(self, pos):
        if self.head is None:
            print("No element")
            return

        if pos < 1:
            print("Invalid Position")
            return

        if pos == 1:
            self.del_first_node()
            return

        temp = self.head
        count = 1

        while temp is not None and count < pos:
            temp = temp.next
            count += 1

        if temp is None:
            print("Position out of range")
            return

        if temp.next is not None:
            temp.next.prev = temp.prev

        if temp.prev is not None:
            temp.prev.next = temp.next


    # Display
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


# Main program
if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.insert_at_begin(20)
    dll.insert_at_begin(10)
    dll.insert_at_begin(30)
    dll.insert_at_begin(40)

    print("Original List:")
    dll.display()

    print("\nAfter deletion at beginning:")
    dll.del_first_node()
    dll.display()

    print("\nAfter deletion at end:")
    dll.del_at_end()
    dll.display()

    print("\nAfter deletion at position 2:")
    dll.del_at_position(2)
    dll.display()