import asyncio
import time


# Synchronous
def synchronous():
    print("Synchronous started")

    time.sleep(2)
    print("Task 1 completed")

    time.sleep(2)
    print("Task 2 completed")


# Asynchronous
async def task(name, seconds):
    print(name, "started")
    await asyncio.sleep(seconds)
    print(name, "completed")


async def asynchronous():
    print("Asynchronous started")

    await asyncio.gather(
        task("Task 1", 2),
        task("Task 2", 2)
    )


print("SYNCHRONOUS")
start = time.perf_counter()
synchronous()
print("Time:", time.perf_counter() - start, "seconds")


print("\nASYNCHRONOUS")
start = time.perf_counter()
asyncio.run(asynchronous())
print("Time:", time.perf_counter() - start, "seconds")