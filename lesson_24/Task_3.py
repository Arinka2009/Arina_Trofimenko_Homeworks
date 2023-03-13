class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()

    def get_from_stack(self, e):  # for Stack and Queue method 'get_from_stack' the same
        if e in self._items:
            i = self._items.index(e)
            self._items = self._items[:i] + self._items[i + 1:]
            return e
        else:
            raise ValueError(f'"{e}" is not on the stack')


class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()

    def get_from_queue(self, e):  # for Stack and Queue my method 'get_from_stack' will be the same
        if e in self._items:
            i = self._items.index(e)
            self._items = self._items[:i] + self._items[i + 1:]
            return e
        else:
            raise ValueError(f'"{e}" is not in the queue')


if __name__ == "__main__":
    s = Stack()
    s.push(4)
    s.push('darken')
    s.push(10)
    s.push('arina')
    s.push(25)
    print(s.get_from_stack(25))
    print(s.get_from_stack('arina'))
    print(s)

    q = Queue()
    q.enqueue(4)
    q.enqueue('darken')
    q.enqueue(10)
    q.enqueue('arina')
    q.enqueue(25)
    print(q.get_from_queue(25))
    print(q.get_from_queue('arina'))
    print(q)
    print(q.get_from_queue(True))  # Value Error
