import time
from concurrent.futures import ThreadPoolExecutor


def func(value):
    time.sleep(1)
    print(value)

pool = ThreadPoolExecutor(max_workers=5)

for i in range(20):
    fut = pool.submit(func, i)
    print(fut)