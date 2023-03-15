# Task 2nd

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.__workers = []

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.__workers.append(worker)
        else:
            raise ValueError("The worker must be an instance of Worker class")


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: 'Boss'):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss

    @property
    def boss(self):
        return self.__boss

    @boss.setter
    def boss(self, value):
        if isinstance(value, Boss):
            self.__boss = value
        else:
            raise ValueError("The boss must be an instance of Boss class")


# create two Boss instances
boss1 = Boss(1, "John Doe", "Acme Inc")
boss2 = Boss(2, "Jane Smith", "XYZ Corp")

# create  Worker instances
worker1 = Worker(101, "Alice", "Acme Inc", boss1)
worker2 = Worker(102, "Bob", "Acme Inc", boss1)
worker3 = Worker(103, "Charlie", "XYZ Corp.", boss2)

# Check the code
worker2.boss = boss2
print(worker2.boss.id, worker2.boss.name)  # --> 2, Jane Smith

boss3 = None
worker1.boss = boss3  # --> ValueError: The boss must be an instance of Boss class

boss1.add_worker(worker3)  # add Worker(103, "Charlie", "XYZ Corp.", boss2) to list "workers" of boss1

worker4 = None
boss2.add_worker(worker4)  # --> ValueError: The worker must be an instance of Worker class

