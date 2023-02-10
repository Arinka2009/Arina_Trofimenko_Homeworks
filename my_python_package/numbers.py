from squared_num import squared

num = [2, 5, 3, 6, 12, 21, 40]

cubing = list(map(lambda x, y: x * y, squared(num), num))
dict_cubing_num = {num: cubing for num, cubing in zip(num, cubing)}
print(f'Cubing of our numbers are: {dict_cubing_num}')
