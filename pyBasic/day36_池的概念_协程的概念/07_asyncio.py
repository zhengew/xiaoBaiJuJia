import asyncio

async def func(name):
    print('start', name)
    # await 可能会发生阻塞的方法
    # await 关键子必须写在一个async函数里
    await asyncio.sleep(1)
    print('end')

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([func('alex'), func('tbjx')]))
