class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next= None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
    #insert at beginning
    def insert_at_begin(self,data):
        new_node= Node(data)

        if self.head is not None:
            new_node.next=self.head
            self.head.prev=new_node

        self.head=new_node

    def insert_at_end(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return
        temp=self.head

        while temp.next is not None:
            temp=temp.next

        temp.next=new_node
        new_node.prev=temp

    def insert_at_position(self,data,pos):
        new_node=Node(data)

        if pos==1:
            new_node.next=self.head

            if self.head is not None:
                self.head.prev=new_node

            self.head=new_node
            return
        temp=self.head

        for i in range(1,pos - 1):
            if temp is None:
                print("Invalid Position")
                return
            temp=temp.next

        if temp is None:
            print("Invalid Position")
            return
        new_node.next=temp.next
        new_node.prev=temp

        if temp.next is not None:
            temp.next.prev=new_node

        temp.next=new_node



#display
    def display(self):
     temp=self.head

     while temp is not None:
            print(temp.data, end=" <-> ")
            temp=temp.next

     print("None")


#Main program
if __name__=="__main__":
    dll=DoublyLinkedList()
    print("Insert at beginning:")
    dll.insert_at_begin(20)
    dll.insert_at_begin(10)
    dll.display()

    print("Insertion at position 2:")
    dll.insert_at_position(100,2)
    dll.display()

    print("Insert at end:")
    dll.insert_at_end(30)
    dll.display()


              
