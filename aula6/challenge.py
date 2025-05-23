# Challenge Session 6: Asynchronous Rate Limiter
# Problem: Implement an asynchronous rate limiter that allows only a fixed number of tasks per second.
# Hint: Use an asyncio semaphore to control the concurrency.

import asyncio
import time

class RateLimiter:
    def __init__(self, max_tasks_per_second):
        self.semaphore = asyncio.Semaphore(max_tasks_per_second)
        self.max_tasks_per_second = max_tasks_per_second

    async def __aenter__(self):
        await self.semaphore.acquire()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await asyncio.sleep(1 / self.max_tasks_per_second)
        self.semaphore.release()

async def limited_task(name, limiter):
    async with limiter:
        print(f"{name} started at {time.strftime('%X')}")
        await asyncio.sleep(0.5)
        print(f"{name} finished at {time.strftime('%X')}")

async def main():
    limiter = RateLimiter(3)  # Allow 3 tasks per second
    tasks = [limited_task(f"Task {i+1}", limiter) for i in range(10)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
