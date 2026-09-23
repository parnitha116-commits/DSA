'''class StackEx:
    def __init__(self, size):
        self.size=size
        self.stack=[None]*size
        self.top = -1
    def push(self,item):
        if self.top == self.size - 1:
            print("stack overflow")
        else:
            self.top+=1
            self.stack[self.top]=item
            print(item,"pushed into the stack")
    def pop(self):
        if self.top == -1:
            print("stack underflow")
        else:
            item = self.stack[self.top]
            self.stack[self.top]=None
            self.top-=1
            print(item,"popped from the stack")
    def peek(self):
        if self.top == -1:
            print("stack is empty")
        else:
            print("Top Element:",self.stack[self.top])
    def display(self):
        if self.top == -1:
            print("stack is empty")
        else:
            print("The elements of the stack are:")
            for i in range(self.top,-1,-1):
                print(self.stack[i])
size=int(input("enter the size of the stack:"))
s = StackEx(size)
while True:
    print("\n---------Stack Menu---------\n")
    print("1.push\n")
    print("2.pop\n")
    print("3.peek\n")
    print("4.display")
    choice = int(input("Enter the choice(1 to 5):"))
    if choice == 1:
        item = int(input("enter the element to push:"))
        s.push(item)
    elif choice == 2:
        s.pop()
    elif choice == 3:
        s.peek()
    elif choice == 4:
        s.display()
    elif choice == 5:
        print("Programme terminated")
        break
    else:
        print("Invalid choice")
        '''

#stack using linked list:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new = Node(data)
        new.next = self.top
        self.top = new
        print(data, "Pushed into stack")

    def pop(self):
        if self.top is None:
            print("Stack underflow")
        else:
            temp = self.top
            print(temp.data, "popped from stack")
            self.top = self.top.next

    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top
            print("Stack elements:")
            while temp is not None:
                print(temp.data)
                temp = temp.next


s = Stack()

while True:
    print("\n------ Stack using Linked List ------")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter the choice: "))

    if choice == 1:
        data = int(input("Enter the element: "))
        s.push(data)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        s.display()

    elif choice == 5:
        print("Programme terminated")
        break

    else:
        print("Invalid choice")















































