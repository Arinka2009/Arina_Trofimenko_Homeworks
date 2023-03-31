class MyHashTable:
    def __init__(self, length=5):
        self.array = [[] for _ in range(length)]
        self.length = length

    def hash_function(self, key):
        length = len(self.array)
        return hash(key) % length

    def set(self, key, value):
        index = self.hash_function(key)
        self.array[index].append((key, value))

    def __contains__(self, key):
        index = self.hash_function(key)
        sublist = self.array[index]
        for dict_key, dict_value in sublist:
            if dict_key == key:
                return True
        return False

    def __len__(self):
        # Count the number of key-value pairs stored in the hash table
        return sum(len(sublist) for sublist in self.array)


my_hash_table = MyHashTable()
my_hash_table.set('apple', 1)
my_hash_table.set('banana', 2)
my_hash_table.set('cherry', 3)
my_hash_table.set('peach', 4)


# Check if the hash table contains a specific key
print('YES' if 'apple' in my_hash_table else 'NO')  # YES
print('YES' if 'orange' in my_hash_table else 'NO')  # NO

# Get the length of the hash table
print(len(my_hash_table))  # 4
print(my_hash_table.array)
