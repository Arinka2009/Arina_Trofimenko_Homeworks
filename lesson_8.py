# Task 1
def favorite_movie(movie_name):
    print(f'My favorite movie is named: "{movie_name}".')


favorite_movie('5th element')


# Task 2
def make_country(name, capital):
    country_dict = {name: capital}
    print(country_dict)


make_country('Ukraine', 'Kyiy')


# Task 3
def make_operation(arithmetic_operator, *args):
    if len(args) == 0:
        return 'Error'
    for item in args:
        if type(item) != int and type(item) != float:
            return 'Error'

    result = args[0]
    for item in args[1:]:
        if arithmetic_operator == '+':
            result += item
        elif arithmetic_operator == '-':
            result -= item
        elif arithmetic_operator == '*':
            result *= item
        else:
            return 'Error'
    return result


# just check results
print(make_operation('*', 7, 6))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('+', 7, 7, 2))
print(make_operation('/', 12, -2))
print(make_operation('-'))
print(make_operation('+', 'y', -2))
