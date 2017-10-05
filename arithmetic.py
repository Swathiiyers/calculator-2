"""Math functions for calculator."""


def add(numbers_list):
    """Return the sum of the two inputs."""

    result = 0
    for i in numbers_list:
        result += i
    return result


def subtract(numbers_list):
    """Return the second number subtracted from the first."""

    result = numbers_list[0]
    for i in numbers_list:
        result -= i 
    return result


def multiply(numbers_list):
    """Multiply all inputs together."""
    answer = 0
    for i in numbers_list:
        answer *= i 
    return answer


def divide(numbers_list):
    """Divide the first input by the second and return the result."""
    result = numbers_list[0]
    new_result = 0
    for i in numbers_list[1:]:
        new_result = result / i
    return new_result



def square(numbers_list):
    """Return the square of the input."""

    if len(numbers_list) == 1:
        return (numbers_list[0]*numbers_list[0])
    print "Wrong number of operands. Try again."
    # Needs only one argument



def cube(num1):
    """Return the cube of the input."""

    # Needs only one argument

    return num1 * num1 * num1


def power(num1, num2):
    """Raise num1 to the power of num and return the value."""

    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    """Return the remainder of num / num2."""

    return num1 % num2
