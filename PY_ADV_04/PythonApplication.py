import time

start_time = time.perf_counter()

total = 0

for i in range(1, 1000001):
    total = total + i

end_time = time.perf_counter()

execution_time = end_time - start_time

print("Total:", total)
print("Execution time:", execution_time, "seconds")