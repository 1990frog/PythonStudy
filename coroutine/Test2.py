import asyncio

async def others():
    print("start")
    await asyncio.sleep(2)
    print("end")
    return 'haha'

async def func():
    print("执行协程函数内部代码")

    # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行，当前协程挂起时，事件循环可以去执行其他协城（任务）
    response = await others()

    print("IO请求结束，结果为：",response)

asyncio.run(func())