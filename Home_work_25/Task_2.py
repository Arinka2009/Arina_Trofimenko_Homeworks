class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    # Adds item to the start of the stack
    def push(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # Remove item that is the current head (start of the stack)
    def pop(self):
        if self.is_empty():
            return f'Stack is empty'
        else:
            # Removes the head node and makes previous one the new head
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data

    # Returns the head of stack
    def peek(self):
        if self.is_empty():
            return f'Stack is empty'
        else:
            return self.head.data
        # size of the list

    # Returns len of stack
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    # Prints out the stack
    def display(self):
        current_node = self.head
        if self.is_empty():
            return None
        while current_node:
            print(current_node.data, end="; ")
            current_node = current_node.next
        print()
        return None


if __name__ == "__main__":
    MyStack = Stack()

    print(MyStack.is_empty())  # == True

    MyStack.push(1)
    MyStack.push(2)
    MyStack.push(3)
    MyStack.push(4)

    MyStack.display()  # 4; 3; 2; 1;

    print("\nTop element is ", MyStack.peek())  # Top element is  4

    print(MyStack.pop())  # == 4
    print(MyStack.pop())  # == 3

    MyStack.display()  # 2; 1;

    print("\nTop element is ", MyStack.peek())  # Top element is  2
