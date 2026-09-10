# Generator and iterator example

def number_generator():
    for number in range(1, 4):
        yield number


numbers = number_generator()

for number in numbers:
    print(number)