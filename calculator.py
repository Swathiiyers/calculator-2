"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


def calculator (tokenized_input):
    """Creates a basic prefix calculator.

    Inputs floats and returns the result of the arithemtic operation."""
    

    operation = tokenized_input[0]
    num_1 = float(tokenized_input[1])
    try:
        num_2 = float(tokenized_input[2])
    except:
        pass
    
    if operation == "+":
        return add(num_1, num_2)
    elif operation  == "-":
        return subtract(num_1, num_2)
    elif operation == "*":
        return multiply (num_1, num_2)
    elif operation == "/":
        return divide(num_1, num_2)
    elif operation == "square":
        return square(num_1)
    elif operation == "cube":
        return cube(num_1)
    elif operation == "pow":
        return power(num_1, num_2)
    elif operation == "mod":
        return mod(num_1, num_2)

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