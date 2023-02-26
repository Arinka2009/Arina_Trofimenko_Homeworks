# 1st Task

class Person:
    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f'SchoolMember: {self.firstname} {self.lastname}\nAge: {self.age} years\n'

    def speak(self, message: str):
        print(f'{self.firstname} {self.lastname} says: {message}')


class Teacher(Person):
    def __init__(self, firstname, lastname, age, discipline, monthly_salary):
        Person.__init__(self, firstname, lastname, age)
        self.discipline = discipline
        self.monthly_salary = monthly_salary

    def year_salary(self):
        print(f'{self.firstname} {self.lastname} gets year salary: ${self.monthly_salary * 12}')
        return self.monthly_salary * 12

    def teach(self):
        print(f'{self.firstname} {self.lastname} is teaching discipline: {self.discipline}')
        return self.discipline


class Student(Person):
    def __init__(self, firstname, lastname, age, year_of_university):
        Person.__init__(self, firstname, lastname, age)
        self.year_of_university = year_of_university

    def study(self):
        print(f'{self.firstname} {self.lastname} is studying.')

    def years_before_graduation(self):
        years_before_graduation = 5 - self.year_of_university
        if years_before_graduation > 0:
            print(f'{years_before_graduation} year(s) left until graduation: {years_before_graduation}')
        else:
            print(f'{self.firstname} {self.lastname} will be graduated this year')
        return years_before_graduation


# objects
person_1 = Person("Parks", "Bryan", 55)
person_2 = Teacher("Winnie", "Roberson", 46, "History and Law", 1500)
person_3 = Teacher("Reed", "Mcneil", 50, "Marketing", 1000)
person_4 = Student("Petty", "Baird", 21, 2)
person_5 = Student("Montgomery", "Knox", 23, 4)
