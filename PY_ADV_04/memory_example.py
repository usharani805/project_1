import sys

number = 100
name = "Python"
numbers = [1, 2, 3, 4, 5]

print("Memory used by number:", sys.getsizeof(number), "bytes")
print("Memory used by name:", sys.getsizeof(name), "bytes")
print("Memory used by list:", sys.getsizeof(numbers), "bytes")