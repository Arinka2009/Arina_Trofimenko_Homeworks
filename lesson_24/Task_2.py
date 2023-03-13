from stack import Stack

type_of_out_bracket = ['(', '{', '[']
type_of_close_bracket = [')', '}', ']']
pairs_of_brackets = ['()', '{}', '[]']

def check_brackets_balance(string: str):
    stack = Stack()  # Create an empty stack

    for char in string:
        if char in type_of_out_bracket:
            stack.push(char)
        elif char in type_of_close_bracket:
            if stack.is_empty() or stack.peek() + char not in pairs_of_brackets:
                return False
            else:
                stack.pop()

    if stack.is_empty():
        return True
    return False


if __name__ == "__main__":
    input_string = input("<<< Enter a sequence of characters >>>\n")
    if check_brackets_balance(input_string):
        print("Brackets are balanced")
    else:
        print("Brackets are not balanced")
        
        
