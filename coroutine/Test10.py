import asyncio
import concurrent.futures
import time


def func1():
    time.sleep(2)
    return "SB"


async def main():
    loop = asyncio.get_running_loop()

    # 1.Run is the default loop's executor (默认ThreadPoolExecutor)
    # 第一步：内部会先调用 ThreadPoolExecutor 的 submit 方法去线程池去执行func1函数，并返回一个concurrent.futures.Future对象
    # 第二步：调用 asyncio.wrap_future将concurrent.futures.Future 对象包装为 asycio.Future 对象
    # 因为 concurrent.futures.Future 对象不支持await语法，所以需要包装为 asycio.Future 对象才能使用。
    fut = loop.run_in_executor(None, func1)
    result = await fut
    print('default thread pool', result)

    # 2.Run in a custom thread pool:
    # with concurrent.futures.ThreadPoolExecutor() as pool:
    #     result = await  loop.run_in_executor(pool, func1)
    #     print('custom thread pool', result)

    # 3.Run in a custom process pool:
    # with concurrent.futures.ProcessPoolExecutor() as pool:
    #     result = await loop.run_in_executor(pool, func1)
    #     print('custom process pool', result)
