import asyncio
import functools
import threading
import time

import aiohttp
import requests


async def get_num_async(number):
    for i in range(1, number+1):
        print(f"{number} 중 {i}")
        # time.sleep(1)
        # await asyncio.sleep(1)  # 1초 동안 대기

def get_num(number):
    for i in range(1, number+1):
        # time.sleep(0.3)
        # await asyncio.sleep(1)  # 1초 동안 대기
        print(f"{number} 중 {i}")

# asyncio를 사용한 비동기 함수
async def async_task(number):
    print(f"Start async task {number}")
    # time.sleep(2)  # 1초 동안 대기
    await get_num_async(number)
    print(f"Async task {number} completed")

def loop_task(number):
    print(f"Start loop task {number}")
    # time.sleep(2)  # 1초 동안 대기
    get_num(number)
    print(f"loop task {number} completed")


async def main_asyncio():
    print("Asyncio example:")
    await asyncio.gather(async_task(2), async_task(3), async_task(4))

async def loop_asyncio():
    tasks = [
        asyncio.create_task(async_task(2)),
        asyncio.create_task(async_task(3)),
        asyncio.create_task(async_task(4))
    ]
    await asyncio.gather(*tasks)

# 스레드를 사용한 병렬 실행 함수
def thread_task(number):
    print(f"Start thread task {number}")
    for i in range(1, number+1):
        res = requests.get(url="https://www.naver.com")
        print(f"{number} 중 {i}")
        # time.sleep(.1)  # 1초 동안 대기
    print(f"Thread task {number} completed")

def main_threading():
    print("Threading example:")
    thread1 = threading.Thread(target=thread_task, args=(2,))
    thread2 = threading.Thread(target=thread_task, args=(3,))
    thread3 = threading.Thread(target=thread_task, args=(4,))
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()

async def sub_async_task(number):
    print(f"Start async task {number}")
    for i in range(1, number+1):
        res = requests.get(url="https://www.naver.com")
        print(f"{number} 중 {i}")
        # time.sleep(.1)
        # await asyncio.sleep(.5)  # 비동기적으로 대기
    # get_num(number)
    print(f"Async task {number} completed")

async def sub_async_task_aiohttp(number):
    connector = aiohttp.TCPConnector(ssl=False)  # SSL 검증 비활성화
    async with aiohttp.ClientSession(connector=connector) as session:
        for i in range(1, number+1):
            async with session.get(url="https://www.naver.com") as response:
                print(f"{number} 중 {i}")
        print(f"Async task {number} completed")

async def sub_asyncio():
    print("Asyncio example:")
    tasks = [
        sub_async_task(2),
        sub_async_task(3),
        sub_async_task(4)
    ]
    await asyncio.gather(*tasks)

async def sub_asyncio_aiohttp():
    print("AioHttp example:")
    tasks = [
        sub_async_task_aiohttp(2),
        sub_async_task_aiohttp(3),
        sub_async_task_aiohttp(4)
    ]
    await asyncio.gather(*tasks)

asyncio.run(sub_asyncio())
print("-------------------------------------")
asyncio.run(sub_asyncio_aiohttp())
