from sys import path

def count_lines(file_name):
    file = open(file_name, 'r')
    total_lines = len(file.readlines())
    print(total_lines)


def count_chars(file_name):
    file = open(file_name, 'r')
    total_chars = len(file.read())
    print(total_chars)



def test(file_name):
    try:
        count_lines(file_name)
        count_chars(file_name)
    except FileNotFoundError:
        print(f"Cannot open the file '{file_name}'")



test(input('Please enter the filepath: '))
