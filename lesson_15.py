# 1st Task
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f'"Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old."')


object_1 = Person('Carl', 'Johnson', 26)

object_1.talk()  # checking the code


# 2nd Task
class Dog:
    def __init__(self, dog_age):
        self.age_factor = 7
        self.dog_age = dog_age

    def human_age(self):
        human_age = self.age_factor * self.dog_age
        print(f'Dog’s age {self.dog_age} in human equivalent will be {human_age} years old.')
        return human_age


dog_1 = Dog(2)

dog_1.human_age()


# 3rd Task
class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current = channels[0]

    def first_channel(self):
        self.current = self.channels[0]
        return self.current

    def last_channel(self):
        self.current = self.channels[-1]
        return self.current

    def turn_channel(self, channel_number):
        self.current = self.channels[channel_number - 1]
        return self.current

    def find_channel_index(self, channel):
        return self.channels.index(channel)

    def next_channel(self):
        if self.current == self.channels[-1]:
            return self.first_channel()
        else:
            self.current = self.channels[self.find_channel_index(self.current) + 1]
            return self.current

    def previous_channel(self):
        if self.current == self.channels[0]:
            return self.last_channel()
        else:
            self.current = self.channels[self.find_channel_index(self.current) - 1]
            return self.current

    def current_channel(self):
        return self.current

    def is_exist(self, channel):
        if isinstance(channel, str) and channel in self.channels:
            return 'YES'
        if isinstance(channel, int) and channel in list(range(1, len(self.channels) + 1)):
            return 'YES'
        else:
            return 'NO'


controller = TVController(["BBC", "Discovery", "TV1000"])
# Checking the code
print(controller.first_channel())  # == "BBC"
print(controller.last_channel())  # == "TV1000"
print(controller.turn_channel(1))  # == "BBC"
print(controller.next_channel())  # == "Discovery"
print(controller.previous_channel())  # == "BBC"
print(controller.current_channel())  # == "BBC"
print(controller.is_exist(4))  # == "No"
print(controller.is_exist("BBC"))  # == "Yes"

