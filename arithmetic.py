"""Functions for common math operations."""

#Comment testing

def add(num1, num2):
    """Return the sum of the two inputs."""
    sum = num1 + num2
    print("Your answer is",sum)
    return sum


def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    subtract = num1 - num2
    return subtract


def multiply(num1, num2):
    """Multiply the two inputs together."""
    multiply = num1 * num2
    return multiply

def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    divide = num1/num2
    return divide

def square(num1):
    """Return the square of the input."""
    square = num1 ** 2
    return square

def cube(num1):
    """Return the cube of the input."""
    cube = num1 ** 3

def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    power = num1 ** num2
    return power

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    mod = num1 % num2
    return mod

def add_mult(num1, num2, num3):
    """Get the sum of num1 and num2, then multiply sum with num3."""
    add_mult = (num1 + num2) * num3
    return add_mult

def add_cubes(num1, num2):
    """Add the cubes of num1 and num2."""
    add_cubes = num1**3 + num2**3
    return add_cubes