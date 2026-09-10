# Generator example

def number_generator():
    for number in range(1, 4):
        yield number


generator = number_generator()

print(next(generator))
print(next(generator))
print(next(generator))