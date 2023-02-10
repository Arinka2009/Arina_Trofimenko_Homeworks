def squared(a):  # function for getting squared of numbers (return list of squared)
    i = 0
    dict_squared_num = {}
    list_squared_num = []

    for item in a:
        item = int(item ** 2)
        list_squared_num.append(item)
        dict_squared_num.update({a[i]: item})
        i = i + 1
    print(f'Squared of our numbers are: {dict_squared_num}')
    return list_squared_num
