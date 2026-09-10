# Advanced function example
# A function can be passed as an argument to another function.


def add(a, b):
    return a + b


def calculate(a, b, operation):
    return operation(a, b)


result = calculate(10, 5, add)

print("Result:", result)