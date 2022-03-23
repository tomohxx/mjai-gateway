import asyncio
import json
import logging

import websockets


async def consumer_handler(websocket) -> None:
    async for message in websocket:
        # do something
        await asyncio.sleep(1)


async def producer_handler(websocket) -> None:
    for _ in range(3):
        await websocket.send('<Z/>')
        await asyncio.sleep(10)


async def hello() -> None:
    uri = 'wss://b-ww.mjv.jp'
    origin = 'https://tenhou.net'
    extra_headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ja,en-US;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    }

    async with websockets.connect(
            uri,
            ssl=True,
            origin=origin,
            extra_headers=extra_headers) as websocket:
        message = json.dumps({'tag': 'HELO', 'name': 'NoName', 'sx': 'M'})
        await websocket.send(message)
        await asyncio.gather(
            consumer_handler(websocket),
            producer_handler(websocket),
            return_exceptions=True
        )


if __name__ == '__main__':
    logger = logging.getLogger('websockets')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    try:
        asyncio.run(hello())
    except KeyboardInterrupt:
        pass
