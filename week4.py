#single linked list
'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    # 1. Create Linked List
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            data = int(input("Enter data: "))
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.next = new_node

        print("Linked List created successfully")

    # 2. Insert at Beginning
    def insert_beginning(self):
        data = int(input("Enter data: "))

        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning.")
        
    # 3. Insert at End
    def insert_end(self):
        data = int(input("Enter data: "))

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        print(f"Inserted {data} at the end.")

    # 4. Insert at Index
    def insert_at_index(self):
        data = int(input("Enter data: "))
        index = int(input("Enter index: "))

        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(index - 1):
            if temp is None:
                print("Index out of range")
                return
            temp = temp.next

        if temp is None:
            print("Index out of range")
            return

        new_node = Node(data)

        new_node.next = temp.next
        temp.next = new_node
        print(f"Inserted {data} at index {index}.")

    # 5. Delete from Beginning
    def delete_beginning(self):

        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next
        print(f"Deleted beginning node.")

    # 6. Delete from End
    def delete_end(self):

        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next is not None:
            temp = temp.next

        temp.next = None
        print(f"Deleted last node.")

    # 7. Delete from Index
    def delete_at_index(self):

        index = int(input("Enter index: "))

        if self.head is None:
            print("List is empty")
            return

        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(index - 1):
            if temp.next is None:
                print("Index out of range")
                return
            temp = temp.next

        if temp.next is None:
            print("Index out of range")
            return

        temp.next = temp.next.next
        print(f"Deleted the node value.")

    # 8. Count Nodes
    def count_nodes(self):

        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)
    # 9. Display
    def display(self):

        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

   


# Main Program

sll = SLL()

while True:

    print("\n----- SINGLY LINKED LIST -----")
    print("1. Create Linked List")
    print("2. Insert at Beginning")
    print("3. Insert at End")
    print("4. Insert at Index")
    print("5. Delete from Beginning")
    print("6. Delete from End")
    print("7. Delete from Index")
    print("8. Count Number of nodes")
    print("9. Display")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        sll.create()

    elif choice == 2:
        sll.insert_beginning()

    elif choice == 3:
        sll.insert_end()

    elif choice == 4:
        sll.insert_at_index()

    elif choice == 5:
        sll.delete_beginning()

    elif choice == 6:
        sll.delete_end()

    elif choice == 7:
        sll.delete_at_index()

    elif choice == 8:
        sll.count_nodes()

    elif choice == 9:
        sll.display()

    elif choice == 10:
        print("Exiting from the program...")
        break

    else:
        print("Invalid choice")'''

#Double linked list
'''class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

        if self.head:
            self.head.prev = None

    # Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.prev.next = None

    # Display forward
    def display_forward(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    # Display backward
    def display_backward(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")


# Main program
dll = DoublyLinkedList()

while True:

    print("\n----- DOUBLY LINKED LIST -----")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete from Beginning")
    print("4. Delete from End")
    print("5. Display Forward")
    print("6. Display Backward")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        dll.insert_beginning(data)

    elif choice == 2:
        data = int(input("Enter data: "))
        dll.insert_end(data)

    elif choice == 3:
        dll.delete_beginning()

    elif choice == 4:
        dll.delete_end()

    elif choice == 5:
        dll.display_forward()

    elif choice == 6:
        dll.display_backward()

    elif choice == 7:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
'''

# Circular linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # 1. Create a linked list
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            data = int(input("Enter value: "))
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
                new_node.next = self.head
            else:
                temp = self.head

                while temp.next != self.head:
                    temp = temp.next

                temp.next = new_node
                new_node.next = self.head

        print("Linked list created successfully.")

    # 2. Insert at beginning
    def insert_beginning(self):
        data = int(input("Enter value: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

        print("Node inserted at beginning.")

    # 3. Insert at end
    def insert_end(self):
        data = int(input("Enter value: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

        print("Node inserted at end.")

    # 4. Insert at specific index
    def insert_at_index(self):
        index = int(input("Enter index: "))
        data = int(input("Enter value: "))

        new_node = Node(data)

        if index == 0:
            if self.head is None:
                self.head = new_node
                new_node.next = self.head
            else:
                temp = self.head

                while temp.next != self.head:
                    temp = temp.next

                new_node.next = self.head
                temp.next = new_node
                self.head = new_node

            print("Node inserted successfully.")
            return

        if self.head is None:
            print("Invalid index.")
            return

        temp = self.head
        count = 0

        while count < index - 1:
            temp = temp.next
            count += 1

            if temp == self.head:
                print("Invalid index.")
                return

        new_node.next = temp.next
        temp.next = new_node

        print("Node inserted successfully.")

    # 5. Delete by value
    def delete_by_value(self):
        value = int(input("Enter value to delete: "))

        if self.head is None:
            print("List is empty.")
            return

        current = self.head
        previous = None

        while True:
            if current.data == value:

                # Only one node
                if current == self.head and current.next == self.head:
                    self.head = None

                # Delete head
                elif current == self.head:
                    temp = self.head

                    while temp.next != self.head:
                        temp = temp.next

                    self.head = self.head.next
                    temp.next = self.head

                # Delete other node
                else:
                    previous.next = current.next

                print("Node deleted successfully.")
                return

            previous = current
            current = current.next

            if current == self.head:
                break

        print("Value not found.")

    # 6. Delete first node
    def delete_first(self):
        if self.head is None:
            print("List is empty.")
            return

        # Only one node
        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            self.head = self.head.next
            temp.next = self.head

        print("First node deleted.")

    # 7. Delete last node
    def delete_last(self):
        if self.head is None:
            print("List is empty.")
            return

        # Only one node
        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head

            while temp.next.next != self.head:
                temp = temp.next

            temp.next = self.head

        print("Last node deleted.")

    # 8. Count number of nodes
    def count_nodes(self):
        if self.head is None:
            print("Number of nodes: 0")
            return

        count = 1
        temp = self.head.next

        while temp != self.head:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    # 9. Display
    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head

        print("Circular Linked List:")

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(back to head)")


# Main program
cll = CircularLinkedList()

while True:

    print("\n========== CIRCULAR LINKED LIST ==========")
    print("1. Create a linked list")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at a specific index")
    print("5. Delete by value")
    print("6. Delete 1st node")
    print("7. Delete last node")
    print("8. Count no. of nodes")
    print("9. Display")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cll.create()

    elif choice == 2:
        cll.insert_beginning()

    elif choice == 3:
        cll.insert_end()

    elif choice == 4:
        cll.insert_at_index()

    elif choice == 5:
        cll.delete_by_value()

    elif choice == 6:
        cll.delete_first()

    elif choice == 7:
        cll.delete_last()

    elif choice == 8:
        cll.count_nodes()

    elif choice == 9:
        cll.display()

    elif choice == 10:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
        
















































