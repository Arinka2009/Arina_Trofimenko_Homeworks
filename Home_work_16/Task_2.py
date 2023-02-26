# 2nd Task

class Mathematician:
    @staticmethod
    def square_nums(nums: list) -> list:
        return [num ** 2 for num in nums]

    @staticmethod
    def remove_positives(nums: list) -> list:
        return [num for num in nums if num <= 0]

    @staticmethod
    def filter_leaps(dates: list) -> list:
        return [date for date in dates if date % 4 == 0 and (date % 100 != 0 or date % 400 == 0)]


m = Mathematician()

# Checking the code
print(m.square_nums([7, 11, 5, 4]))  # [49, 121, 25, 16]
print(m.remove_positives([26, -11, -8, 13, -90]))  # [-11, -8, -90]
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))  # [1884, 2020]
