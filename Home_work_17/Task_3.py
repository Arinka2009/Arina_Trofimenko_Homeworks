# 3rd Task

import math


class Fraction:

    def __init__(self, numerator: int, denominator: int = 1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        gcd = math.gcd(numerator, denominator)  # нахожу наибольший общий делитель для числителя и знаменателя
        self.top = numerator // gcd  # сокращаю чеслитель
        self.bottom = denominator // gcd  # сокращаю знаменатель

    def __str__(self):
        if self.bottom == 1:
            return f'{self.top}'  # возвращаю  чеслитель, если знаменатель == 1
        elif self.top > self.bottom:
            return f'{self.top // self.bottom}.{self.top % self.bottom}/{self.bottom}'  # целая часть и дробный остаток
        else:
            return f'{self.top}/{self.bottom}'  # обычный вид дроби

    def __add__(self, other):
        new_top = self.top * other.bottom + self.bottom * other.top
        new_bottom = self.bottom * other.bottom
        return Fraction(new_top, new_bottom)

    def __sub__(self, other):
        new_top = self.top * other.bottom - self.bottom * other.top
        new_bottom = self.bottom * other.bottom
        return Fraction(new_top, new_bottom)

    def __mul__(self, other):
        new_top = self.top * other.top
        new_bottom = self.bottom * other.bottom
        return Fraction(new_top, new_bottom)

    def multiply(self, a):  # умножение на целое число "а"
        return Fraction(a * self.top, self.bottom)

    def __truediv__(self, other):
        new_top = self.top * other.bottom
        new_bottom = self.bottom * other.top
        return Fraction(new_top, new_bottom)

    def __gt__(self, other):
        return self.top * other.bottom > other.top * self.bottom

    def __ge__(self, other):
        return self > other or self == other

    def __lt__(self, other):
        return self.top * other.bottom < other.top * self.bottom

    def __le__(self, other):
        return self < other or self == other

    def __eq__(self, other):
        return self.top * other.bottom == other.top * self.bottom

    def __ne__(self, other):
        return self.top * other.bottom != other.top * self.bottom


# Create exemplars for code checking
x = Fraction(1, 2)
y = Fraction(1, 4)
f1 = Fraction(1, 2)
f2 = Fraction(15, 30)
f3 = Fraction(3, 5)
f4 = Fraction(5, 3)
f5 = Fraction(1)
f6 = Fraction(8, 10)
f7 = Fraction(5, 10)

# Checking the code
if __name__ == "__main__":
    print(x + y)  # 3/4 == Fraction(3, 4)
    print(x - y)  # 1/4 == Fraction(1, 4)
    print(x * y)  # 1/8 == Fraction(1, 8)
    print(x.multiply(7))  # 3.1/2 == Fraction(7, 2)
    print(x / y)  # 2 == Fraction(2, 1)
    print(f1 == f2)  # True
    print(f1 != f4)  # True
    print(f2 > f3)  # False
    print(f4 <= f1)  # False
    print(f1 < f5)  # True
    print(f6 > f4)  # False
    print(f1 != f7)  # False
