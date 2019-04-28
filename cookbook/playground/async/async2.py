import asyncio
import async_timeout
import aiohttp
import time
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

# aiohttp客户端实现
async def hello():
    async with aiohttp.ClientSession() as session:
        with async_timeout.timeout(10):
            async with session.get('http://www.sohu.com') as response:
                r = await response.text()
                print(r)


loop = asyncio.get_event_loop()

start = time.time()
loop.run_until_complete(asyncio.wait([hello() for i in range(10)]))
end = time.time() - start
print(end)
loop.close()


