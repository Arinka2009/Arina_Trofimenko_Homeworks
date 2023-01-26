# Task 1: The greatest number

# first version of the solution:
import random
list_1 = [random.randint(1, 25) for _ in range(10)]
print(f'Largest number from a list {list_1}  is: {max(list_1)}')

# second version of the solution:
list_2 = []
while len(list_2) != 10:
    list_2.append(random.randint(1, 25))
print(f'Largest number from a list {list_2}  is: {max(list_2)}')
#
#
#
# Task 2: Exclusive common numbers
# first version of the solution:
import random
first_list = []
second_list = []
new_list = []
counter = 0

while counter < 10:
    first_list.append(random.randint(1, 10))
    second_list.append(random.randint(1, 10))
    counter += 1
print(f'First list: {first_list}\nSecond list: {second_list}')
print(f'New list with exclusive common numbers: {set(first_list).intersection(set(second_list))}')

# second version of the solution:
first_list = []
second_list = []
new_list = []
counter = 0

while counter < 10:
    first_list.append(random.randint(1, 10))
    second_list.append(random.randint(1, 10))
    counter += 1
print(f'First list: {first_list}\nSecond list: {second_list}')
for number in first_list:
    if number in second_list and number not in new_list:
        new_list.append(number)
print(f'New list with exclusive common numbers: {new_list}')
#
#
#
# Task 3: Extracting numbers
list_3 = list(range(1, 101))
res_list = []
i = 0
while i < len(list_3):
    if list_3[i] % 7 == 0 and list_3[i] % 5 != 0:
        res_list.append(list_3[i])
    i = i+1
print(f'Resulted_list: {res_list}')
