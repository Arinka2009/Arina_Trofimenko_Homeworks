# Task 1
import string

s = input('Enter your sentence: ')
# make low characters, delete all punctuation from a string, split a string into a list where each word is a list item
list_of_input_string = s.lower().translate(str.maketrans('', '', string.punctuation)).split()

words_count_dict = {}
for word in list_of_input_string:
    if word not in words_count_dict:
        words_count_dict[word] = 1
    else:
        words_count_dict[word] += 1
print(words_count_dict)
#
#
# Task 2
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}

total_price = 0
show_total_price = True  # variable for print total price  in the end of the loop

for key in stock:
    if key in prices:
        total_price += stock.get(key) * prices.get(key)
    else:  # warning, if we don't have price for stock's product
        print(f'Key {key} doesn\'t exist in dict "prices"')
        show_total_price = False
        break

if show_total_price:
    print(f'Total price of the stock is: {total_price} UAH')
#
#
# Task 3
list_ = [(i, i ** 2) for i in range(1, 11)]
print(list_, '\n', type(list_))
#
#
# Task 4

import calendar

# List with days of week
day_names = list(calendar.day_name)
# List with numbers of days
day_numbers = list(range(1, 8))

dict_1 = {
    day_number: day_names[day_number - 1]
    for day_number in day_numbers
}
print(dict_1)

invert_dict = {
    day_name: day_names.index(day_name) + 1
    for day_name in day_names
}
print(invert_dict)
