import asyncio

async def func():
    print("start")
    await asyncio.sleep(2)
    print("end")
    return 'haha'

async def main():
    print("main open")
    # 创建task对象，将当前func函数任务添加事件循环
    task1 = asyncio.create_task(func())
    task2 = asyncio.create_task(func())
    print("main close")

    # 当执行某协程遇到IO操作时，会自动化切换执行其他任务
    # 此处的await时等待相对应的协程全部执行完毕并获取结果
    ret1 = await task1
    ret2 = await task2
    print(ret1, ret2)

asyncio.run(main())