import timeit

code = """
total = 0
for i in range(100000):
    total = total + i
"""

time_taken = timeit.timeit(code, number=10)

print("Time taken:", time_taken, "seconds")