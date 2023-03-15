# 1st Task

class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print('Woof-Woof!')


class Cat(Animal):
    def talk(self):
        print('Meow!')


def animal_talk(animal: Animal):
    animal.talk()


cat = Cat()
dog = Dog()

# checking the code
if __name__ == '__main__':
    animal_talk(cat)  # == Meow!
    animal_talk(dog)  # ==  Woof-Woof!

