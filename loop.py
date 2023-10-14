import time
import asyncio


NUMBER = 100


async def async_factorial(n):
    if n == 0:
        return 1
    return n * await async_factorial(n - 1)


def sync_factorial(n):
    if n == 0:
        return 1
    return n * sync_factorial(n - 1)


async_start = time.perf_counter()
asyncio.run(async_factorial(NUMBER))
async_time = time.perf_counter() - async_start

sync_start = time.perf_counter()
sync_factorial(NUMBER)
sync_time = time.perf_counter() - sync_start


print(f'{sync_time = }')
print(f'{async_time = }')
print(f'{(async_time > sync_time) = }')
print(f'{(async_time - sync_time) = }')
