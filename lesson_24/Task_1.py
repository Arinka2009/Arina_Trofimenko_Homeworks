from stack import Stack

def reverse(string: str):
    stack = Stack()  # Create an empty stack
    for char in string:  # Push all characters of string to stack
        stack.push(char)

    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string


if __name__ == "__main__":
    input_string = input("<<< Enter a sequence of characters >>>\n")
    print(reverse(input_string))

    
