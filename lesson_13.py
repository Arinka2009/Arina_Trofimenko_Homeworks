# 1st Task

def scope():
    a = "Have"
    b = "a great day!"
    c = "Hello everyone!"
    d = c + a + b
    print(d)


print("Number of local variables available:", scope.__code__.co_nlocals)


# 2nd Task
def city_func(city: str):
    counter = 0

    def count_of_visits():
        nonlocal counter
        counter += 1
        return city, counter

    return count_of_visits


func_call = city_func("Lviv")
print(func_call())
print(func_call())
print(func_call())

# 3d Task
def choose_func(nums: list, func1, func2):
    check_items = all(num >= 0 for num in nums)
    if check_items:
        return func1(nums)
    else:
        return func2(nums)


def square_nums(nums: list):
    return [num ** 2 for num in nums]


def remove_negatives(nums: list):
    return [num for num in nums if num > 0]


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]
print(choose_func(nums1, square_nums, remove_negatives))

