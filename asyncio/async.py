import asyncio

async def go1():
    asyncio.gather(go2())
    asyncio.gather(go3())
    print("go1 running")
    await asyncio.sleep(5)
    print("go1 stoping")

async def go2():
    asyncio.gather(go4())
    print("go2 running")
    await asyncio.sleep(3)
    print("go2 stoping")

async def go3():
    print("go3 running")
    await asyncio.sleep(1)
    print("go3 stoping")

async def go4():
    print("go4 running")
    await asyncio.sleep(2)
    print("go4 stoping")

loop = asyncio.get_event_loop()
c = asyncio.gather(go1())
try:
    loop.run_until_complete(c)
finally:
    loop.close()