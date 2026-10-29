"""class Queue:
    def __init__(self, size):

        self.size = size

        self.queue = [None] * size

        self.front = -1

        self.rear = -1
 
    def enqueue(self, x):

        if self.rear == self.size - 1:

            print("Queue overflow")

        else:

            if self.front == -1:

                self.front = 0

            self.rear += 1

            self.queue[self.rear] = x

            print(f"{x} inserted into the queue")
 
    def dequeue(self):

        if self.front == -1 or self.front > self.rear:

            print("queue underflow")

        else:

            x = self.queue[self.front]

            self.queue[self.front] = None

            self.front += 1

            print(f"{x} deleted from the queue")

            if self.front > self.rear:

                self.front = -1

                self.rear = -1
 
    def peek(self):

        if self.front == -1:

            print("Queue is empty")

        else:

            print("Front elements:", self.queue[self.front])
 
    def display(self):

        if self.front == -1:

            print("Queue is empty")

        else:

            print("the elements of the queue are:")

            for i in range(self.front, self.rear + 1):

                print(self.queue[i])

if __name__ == "__main__":

    size = int(input("Enter the size of the queue: "))

    q = Queue(size)
 
    while True:

        print("\n--- Queue Operations Menu ---")

        print("1. Enqueue")

        print("2. Dequeue")

        print("3. Peek")

        print("4. Display")

        print("5. Exit")
 
        choice = input("Enter your choice (1-5): ")
 
        if choice == '1':

            val = int(input("Enter value to insert: "))

            q.enqueue(val)

        elif choice == '2':

            q.dequeue()

        elif choice == '3':

            q.peek()

        elif choice == '4':

            q.display()

        elif choice == '5':

            print("Exiting program.")

            break

        else:

            print("Invalid choice! Please enter a number between 1 and 5.")"""




















'''class CircularQueue:

    def __init__(self, size):

        self.size = size

        self.queue = [None] * size

        self.front = -1

        self.rear = -1

    def enqueue(self, x):

        if (self.rear + 1) % self.size == self.front:

            print("Queue overflow")

        else:

            if self.front == -1:  

                self.front = 0

                self.rear = 0

            else:

                self.rear = (self.rear + 1) % self.size

            self.queue[self.rear] = x

            print(f"{x} inserted into the queue")

    def dequeue(self):

        if self.front == -1:

            print("Queue underflow")

        else:

            x = self.queue[self.front]

            self.queue[self.front] = None

            if self.front == self.rear:

                self.front = -1

                self.rear = -1

            else:

                self.front = (self.front + 1) % self.size

            print(f"{x} deleted from the queue")

    def peek(self):

        if self.front == -1:

            print("Queue is empty")

        else:

            print("Front element:", self.queue[self.front])

    def display(self):

        if self.front == -1:

            print("Queue is empty")

        else:

            print("The elements of the queue are:")

            i = self.front

            while True:

                print(self.queue[i], end=" ")

                if i == self.rear:

                    break

                i = (i + 1) % self.size

            print()

if __name__ == "__main__":

    size = int(input("Enter the size of the circular queue: "))

    q = CircularQueue(size)

    while True:

        print("\n--- Circular Queue Operations Menu ---")

        print("1. Enqueue")

        print("2. Dequeue")

        print("3. Peek")

        print("4. Display")

        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':

            val = int(input("Enter value to insert: "))

            q.enqueue(val)

        elif choice == '2':

            q.dequeue()

        elif choice == '3':

            q.peek()

        elif choice == '4':

            q.display()

        elif choice == '5':

            print("Exiting program.")

            break

        else:

            print("Invalid choice! Please enter a number between 1 and 5.")'''















class Node:

    def __init__(self, data):

        self.data = data

        self.next = None

class Queue:

    def __init__(self):

        self.front = None

        self.rear = None

    def enqueue(self, x):

        new_node = Node(x)

        if self.rear is None:

            self.front = self.rear = new_node

        else:

            self.rear.next = new_node

            self.rear = new_node

        print(f"{x} inserted into the queue")

    def dequeue(self):

        if self.front is None:

            print("Queue underflow (Queue is empty)")

        else:

            x = self.front.data

            self.front = self.front.next

            if self.front is None:

                self.rear = None

            print(f"{x} deleted from the queue")

    def peek(self):

        if self.front is None:

            print("Queue is empty")

        else:

            print("Front element:", self.front.data)

    def display(self):

        if self.front is None:

            print("Queue is empty")

        else:

            print("The elements of the queue are:")

            current = self.front

            while current:

                print(current.data, end=" -> " if current.next else "")

                current = current.next

            print()  

if __name__ == "__main__":

    q = Queue()
 
    while True:

        print("\n--- Queue (Linked List) Operations Menu ---")

        print("1. Enqueue")

        print("2. Dequeue")

        print("3. Peek")

        print("4. Display")

        print("5. Exit")
 
        choice = input("Enter your choice (1-5): ")
 
        if choice == '1':

            val = int(input("Enter value to insert: "))

            q.enqueue(val)

        elif choice == '2':

            q.dequeue()

        elif choice == '3':

            q.peek()

        elif choice == '4':

            q.display()

        elif choice == '5':

            print("Exiting program.")

            break

        else:

            print("Invalid choice! Please enter a number between 1 and 5.")
