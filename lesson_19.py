# 1st Task
def with_index(iterable: iter, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1


# check the code
my_list = ['apple', 'banana', 'orange']
for index, value in with_index(my_list):
    print(f"{index}: {value}")


# 2nd Task
def in_range(start: int, end: int, step: int = 1):
    if step == 0:
        raise ValueError("in_range() arg 3 must not be zero")
    elif step < 0:
        while start > end:
            yield start
            start += step
    else:
        while start < end:
            yield start
            start += step


# check the code
for i in in_range(5, -2, 0):  # ValueError: in_range() arg 3 must not be zero
    print(i)

for i in in_range(5, -1, -1):
    print(i)  # 0, 1, 2, 3, 4, 5

for i in in_range(-5, -1):
    print(i)  # -5, -4, -3, -2

for i in in_range(10, 0, -2):
    print(i)  # 10, 8, 6, 4, 2


# 3rd Task
class Counter:
    def __init__(self, initial=1):
        self.initial = initial
        self.current = initial

    def __iter__(self):
        return self

    def __next__(self):
        x = self.current
        self.current += 1
        return x

    def __getitem__(self, index):
        return index + self.initial


# check the code

my_counter = Counter(5)

for index, value in enumerate(my_counter):
    if value % 5 == 0:
        print(f"index {index}: {value}")
    if index == 45:
        break

print(my_counter[5])
