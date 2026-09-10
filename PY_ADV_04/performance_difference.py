import time
import asyncio


def synchronous():
    time.sleep(2)
    time.sleep(2)


async def asynchronous():
    await asyncio.gather(
        asyncio.sleep(2),
        asyncio.sleep(2)
    )


# Synchronous time
start = time.perf_counter()
synchronous()
sync_time = time.perf_counter() - start


# Asynchronous time
start = time.perf_counter()
asyncio.run(asynchronous())
async_time = time.perf_counter() - start


print("Performance Comparison")
print("----------------------")
print("Synchronous:", round(sync_time, 2), "seconds")
print("Asynchronous:", round(async_time, 2), "seconds")

if async_time < sync_time:
    print("Asynchronous execution is faster.")
else:
    print("Synchronous execution is faster.")