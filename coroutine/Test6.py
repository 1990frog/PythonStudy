import asyncio


async def func():
    print("start")
    await asyncio.sleep(2)
    print("end")
    return 'haha'


task_list = [
    func(),
    func()
]
#  写在外面会报错，因为没有事件循环
# task_list = [
#     asyncio.create_task(func(), name='n1'),
#     asyncio.create_task(func(), name='n2')
# ]
done, pending = asyncio.run(asyncio.wait(task_list))
print(done)
