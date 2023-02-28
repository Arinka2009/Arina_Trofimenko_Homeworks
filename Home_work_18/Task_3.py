# Task 3rd
from functools import wraps


class TypeDecorators:
    @staticmethod
    def result_to(cls):
        def decorator(f):
            @wraps(f)
            def wrapper(*args, **kwds):
                result = f(*args, **kwds)
                try:
                    return cls(result)
                except (TypeError, ValueError):
                    return result

            return wrapper

        return decorator


# check the code
@TypeDecorators.result_to(int)
def get_age():
    return "27"


print(type(get_age()))  # --> class 'int'


@TypeDecorators.result_to(str)
def get_age():
    return None


print(type(get_age()))  # --> class 'str'


@TypeDecorators.result_to(bool)
def get_age():
    return 15


print(type(get_age()))  # --> class 'bool'


@TypeDecorators.result_to(float)
def get_age():
    return None


print(type(get_age()))  # --> class 'NoneType'
