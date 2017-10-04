"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def make_int_list (tokenized_input):
    numbers_list = []

    for i in tokenized_input[1:]:
        numbers_list.append(int(i)) 
    return numbers_list


def calculator (tokenized_input):
    """Creates a basic prefix calculator.

    Inputs floats and returns the result of the arithemtic operation."""
    
    operation = tokenized_input[0]
    numbers = make_int_list(tokenized_input)

    if operation == "+":
        return add(numbers)
    elif operation  == "-":
        return subtract(numbers)
    elif operation == "*":
        return multiply (numbers)
    elif operation == "/":
        return divide(numbers)
    elif operation == "square":
        return square(numbers)
    elif operation == "cube":
        return cube(numbers)
    elif operation == "pow":
        return power(numbers)
    elif operation == "mod":
        return mod(numbers)

def is_quiter(tokenized_input):
    """ """
    op = tokenized_input[0]
    op = op.lower()
    return 'q' == op

def get_input():
    """ """
    user_input = raw_input("> ")
    tokenized_input = user_input.split(" ")
    return tokenized_input

# print "This is a test:"

def run_calculator():
    """"""
    print "Please enter your operation or press 'q' to quit:"

    while True:  
        tokenized_input = get_input()
        if is_quiter(tokenized_input):
            break 
        result = calculator(tokenized_input)
        print result

if __name__ == "__main__":
    run_calculator()