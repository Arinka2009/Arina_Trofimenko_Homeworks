# Task 1
def favorite_movie(movie_name):
    print(f'My favorite movie is named: "{movie_name}".')

favorite_movie('5th element')


# Task 2
def make_country(name, capital):
    country_dict = {name: capital}
    print(country_dict)

make_country('Ukraine','Kyiv')


# Task 3
def make_operation(arithmetic_operator, *args):
    if len(args) == 0:
        return
    for item in args:
        if type(item) != int and type(item) != float:
            return

    result = args[0]
    for item in args[1:]:
        if arithmetic_operator == '+':
            result += item
        elif arithmetic_operator == '-':
            result -= item
        elif arithmetic_operator == '*':
            result *= item
        else:
            return
    return result

print(make_operation('*', 12, -2))
print(make_operation('-', 12, -2))
print(make_operation('+', 12, -2))
print(make_operation('/', 12, -2))
print(make_operation('-'))
print(make_operation('+', 'y', -2))


