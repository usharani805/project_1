import time
import asyncio


# Synchronous
def synchronous():
    time.sleep(2)
    time.sleep(2)


# Asynchronous
async def asynchronous():
    await asyncio.gather(
        asyncio.sleep(2),
        asyncio.sleep(2)
    )


# Benchmark synchronous
start = time.perf_counter()
synchronous()
sync_time = time.perf_counter() - start


# Benchmark asynchronous
start = time.perf_counter()
asyncio.run(asynchronous())
async_time = time.perf_counter() - start


print("Synchronous time:", sync_time, "seconds")
print("Asynchronous time:", async_time, "seconds")