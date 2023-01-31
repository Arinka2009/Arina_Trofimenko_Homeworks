# Task 1
def oops():
    raise IndexError()


# If we change oops() to raise Key Error instead of Index Error,
# then the program will fail with the KeyError instead 'Congratulations!You've caught Index Error!' message

def catch_func():
    try:
        oops()
    except IndexError:
        print('Congratulations!You\'ve caught Index Error!')


catch_func()


# Task 2
def func():
    while True:
        try:
            a, b = int(input('Please enter first argument: ')), int(input('Please enter second argument: '))
        except ValueError:
            print('You must enter only integer. ')
            continue
        try:
            result = int(a ** 2 / b)
        except ZeroDivisionError:
            print('Cannot divide by zero')
            continue
        return result


func()
