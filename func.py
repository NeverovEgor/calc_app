import math

class Calculator:
    def __init__(self):
        self.memory = 0

    # Basic arithmetic operations
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    def modulus(self, a, b):
        return a % b

    # Trigonometric functions
    def sine(self, angle):
        return math.sin(math.radians(angle))

    def cosine(self, angle):
        return math.cos(math.radians(angle))

    # Power and roots
    def power(self, base, exponent):
        return math.pow(base, exponent)

    def square_root(self, number):
        if number < 0:
            raise ValueError("Cannot compute the square root of a negative number.")
        return math.sqrt(number)

    # Rounding functions
    def floor(self, number):
        return math.floor(number)
