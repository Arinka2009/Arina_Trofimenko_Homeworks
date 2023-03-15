class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.size

    def enqueue(self, new_data):
        new_node = Node(new_data)
        self.size += 1

        if self.is_empty():
            self.head = self.last = new_node
            return
        self.last.next = new_node
        self.last = new_node

    def dequeue(self):
        if self.is_empty():
            return f'Queue is empty'
        else:
            to_return = self.head.data
            self.head = self.head.next
            self.size -= 1
        return to_return

    def display(self):
        current_node = self.head
        if self.is_empty():
            return None

        while current_node:
            print(current_node.data, end="; ")
            current_node = current_node.next
        print()
        return None


if __name__ == '__main__':
    q = Queue()
    print(q.is_empty())  # True

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print(q.size)  # 3

    q.display()  # 10; 20; 30;

    print(q.dequeue())  # 10

    q.display()  # 20; 30;

    print(q.is_empty())  # False
