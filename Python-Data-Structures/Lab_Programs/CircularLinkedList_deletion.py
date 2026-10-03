class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class circularlist:
    def __init__(self):
        self.head = None


    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            new_node.next = self.head
            temp.next = new_node
            self.head = new_node


    # Deletion at beginning
    def del_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        self.head = self.head.next
        temp.next = self.head


    # Deletion at end
    def del_at_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head

        while temp.next.next != self.head:
            temp = temp.next

        temp.next = self.head


    # Deletion at given position
    def del_at_position(self, pos):
        if self.head is None:
            print("List is empty")
            return

        if pos < 1:
            print("Invalid Position")
            return

        if pos == 1:
            self.del_at_beginning()
            return

        temp = self.head
        count = 1

        while count < pos - 1 and temp.next != self.head:
            temp = temp.next
            count += 1

        if count != pos - 1 or temp.next == self.head:
            print("Position out of range")
            return

        temp.next = temp.next.next


    # Display
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(Head)")


# Main program
if __name__ == "__main__":
    cll = circularlist()

    cll.insert_at_beginning(40)
    cll.insert_at_beginning(30)
    cll.insert_at_beginning(20)
    cll.insert_at_beginning(10)

    print("Original List:")
    cll.display()

    print("\nAfter deletion at beginning:")
    cll.del_at_beginning()
    cll.display()

    print("\nAfter deletion at end:")
    cll.del_at_end()
    cll.display()

    print("\nAfter deletion at position 2:")
    cll.del_at_position(2)
    cll.display()