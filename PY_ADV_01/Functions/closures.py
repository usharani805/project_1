# Simple closure example

def create_multiplier(number):
    def multiply(value):
        return value * number

    return multiply


double = create_multiplier(2)

print(double(5))