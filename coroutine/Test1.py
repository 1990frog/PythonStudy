import asyncio

# 协程函数
async def func(id):
    if id == 'id1':
        await asyncio.sleep(5)
    for i in range(100):
        print(id+":"+str(i))

if __name__ == "__main__":
    asyncio.run(func("id1"))
    asyncio.run(func("id2"))

# # 协程对象
# # 执行协程函数创建协程对象，函数内部代码不会执行
# # 如果想要运行协程函数内部代码，必须要讲协程对象交给事件循环来处理
# result = func()
#
# # 写法1
# # 去生成或获取一个事件循环
# # 将任务放到循环事件中
# # loop = asyncio.get_event_loop()
# # loop.run_unit_complete(result)
#
# # 写法2 py3.7+
# asyncio.run(result)