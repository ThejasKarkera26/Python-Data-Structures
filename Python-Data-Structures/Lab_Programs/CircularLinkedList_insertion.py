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


    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head


    # Insert at given position
    def insert_at_position(self, data, pos):
        if pos < 1:
            print("Invalid Position")
            return

        if pos == 1:
            self.insert_at_beginning(data)
            return

        if self.head is None:
            print("Position out of range")
            return

        new_node = Node(data)
        temp = self.head
        count = 1

        while count < pos - 1 and temp.next is not self.head:
            temp = temp.next
            count += 1

        if count != pos - 1:
            print("Position out of range")
            return

        new_node.next = temp.next
        temp.next = new_node


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


if __name__ == "__main__":
    cll = circularlist()

    print("Insert at beginning:")
    cll.insert_at_beginning(20)
    cll.insert_at_beginning(10)
    cll.display()

    print("\nInsert at end:")
    cll.insert_at_end(30)
    cll.display()

    print("\nInsert at position 2:")
    cll.insert_at_position(15, 2)
    cll.display()