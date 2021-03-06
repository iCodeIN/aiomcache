import asyncio
import aiomcache


loop = asyncio.get_event_loop()


@asyncio.coroutine
def hello_aiomcache():
    mc = aiomcache.Client("127.0.0.1", 11211, loop=loop)
    yield from mc.set(b"some_key", b"Some value")
    value = yield from mc.get(b"some_key")
    print(value)
    values = yield from mc.multi_get(b"some_key", b"other_key")
    print(values)
    yield from mc.delete(b"another_key")


loop.run_until_complete(hello_aiomcache())
