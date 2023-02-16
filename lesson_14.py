# 1st Task
def logger(fun):
    def wrapper(*args, **kvargs):
        print(f'Function "{fun.__name__}"  with params: {args or kvargs}')
        return fun(*args, **kvargs)
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


# Checking function
square_all(2, 3, 4, 5, 6, 7, 8, 9)
add(4, 7)
add(y=4, x=7)


# 2nd Task

def stop_words(words: list):
    def decorator_passing_arguments(function_to_decorate):
        def wrapper_accepting_arguments(name):
            slogan = function_to_decorate(name)
            for word in words:
                slogan = slogan.replace(word, '*')
            print(slogan)  # check what will be returned
            return slogan
        return wrapper_accepting_arguments
    return decorator_passing_arguments


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


# Checking function
create_slogan('Helga')


# 3d Task

def arg_rules(type_: type, max_length: int, contains: list):
    def inner(func):
        def wrapper(name):
            validation_res = False
            if type(name) == type_:
                if len(name) <= max_length:
                    for item in contains:
                        if item in name:
                            validation_res = True
                        else:
                            print(f'"{item}" is missing in "{name}"')
                else:
                    print(f'The length of "{name}" is {len(name)}. It\'s longer than the requested length {max_length}')
            else:
                print(f'type of "{name}" - {type(name)} doesn\'t match with requested {type_}')
            if validation_res:
                return func(name)
            else:
                return validation_res

        return wrapper

    return inner


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


# Checking function
print(create_slogan(15463))
print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('dandelion.com'))
print(create_slogan('S@SH05'))
