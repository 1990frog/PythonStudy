import asyncio


async def func():
    print("start")
    await asyncio.sleep(2)
    print("end")
    return 'haha'


async def main():
    print("main open")
    # 创建task对象，将当前func函数任务添加事件循环

    task_list = [
        asyncio.create_task(func(), name='n1'),
        asyncio.create_task(func(), name='n2')
    ]
    print("main close")

    done, pending = await asyncio.wait(task_list)
    # done, pending = await asyncio.wait(task_list,timeout=1)
    # done, pending = await asyncio.wait(task_list,timeout=None)
    print(done)


asyncio.run(main())
