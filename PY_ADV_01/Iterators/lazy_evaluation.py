# Example 2: Lazy evaluation

def generate_numbers():
    for number in range(1, 4):
        print("Generating:", number)
        yield number


numbers = generate_numbers()

print("Generator created")

print(next(numbers))
print(next(numbers))