class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class UnorderedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, index: int, data):
        new_node = Node(data)

        if index == 0:
            new_next = self.head
            self.head = new_node
            self.head.next = new_next
            self.length += 1
            return self.head

        prev = self.by_index(index - 1)
        if prev is None:
            raise ValueError("Index is out of range")
        _next = prev.next
        prev.next = new_node
        new_node.next = _next
        self.length += 1

        return new_node

    # Add item to and of the list
    def append(self, new_data):
        return self.insert(self.length, new_data)

    def last(self):
        if self.length == 0:
            return None
        return self.by_index(self.length - 1)

    def get_index(self, data):
        current = self.head
        index = 0

        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1

        return None

    def by_index(self, index: int):
        current = self.head
        i = -1
        while current:
            i += 1
            if i == index:
                return current
            if current.next:
                current = current.next
                continue
            return None

    def pop(self, position=None):
        if self.head is None:
            raise ValueError("List is empty")

        if position is None:
            position = self.length - 1

        if position == 0:
            node = self.head
            if self.length == 1:
                self.head = None
                self.length -= 1
                return node
            self.head = node.next
            self.length -= 1
            return node

        prev = self.by_index(position - 1)
        if prev is None or prev.next is None:
            raise ValueError("Index is out of range")

        current = prev.next
        _next = current.next
        prev.next = _next

        self.length -= 1
        return current

    def slice(self, start=0, stop=None):
        if stop is None:
            stop = self.length

        current = self.by_index(start)
        if current is None:
            raise ValueError("Start is out of range")
        if start > stop:
            raise ValueError("Start can't be smaller than the Stop")

        new_list = UnorderedList()
        new_list.append(current.data)

        index = start
        while current.next:
            index += 1
            if index == stop:
                break
            current = current.next
            if current:
                new_list.append(current.data)

        if index < stop - 1:
            raise ValueError("Stop is out of range")

        return new_list

    def __repr__(self):
        result = ''
        temp = self.head
        while temp:
            result += f'{temp.data} -> '
            temp = temp.next
        return result

    def print_list(self):
        print(self)
        return None


if __name__ == '__main__':
    mylist = UnorderedList()
    mylist.insert(0, 'five')
    mylist.append(6)
    mylist.append(7)

    mylist.insert(3, 8)
    mylist.insert(0, 3)
    mylist.insert(1, 4)

    mylist.print_list()  # 3 -> 4 -> five -> 6 -> 7 -> 8 ->

    print(mylist.pop(0))  # Node(3)
    print(mylist.pop())  # Node(8)

    mylist.append('eight')
    mylist.print_list()  # 4 -> five -> 6 -> 7 -> eight ->

    print(mylist.get_index('five'))  # 1
    print(mylist.get_index(4))  # 0

    print(mylist.by_index(0))  # Node(4)

    mylist.slice().print_list()  # 4 -> five -> 6 -> 7 -> eight ->
    mylist.slice(1, 4).print_list()  # five -> 6 -> 7 ->

    mylist.slice(5, 1).print_list()  # ValueError: Start is out of range
    mylist.slice(0, 5).print_list()  # ValueError: Start is out of range
    mylist.slice(-1, 3).print_list()  # ValueError: Start is out of range
