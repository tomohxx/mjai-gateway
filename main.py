import argparse
import asyncio
import datetime
import json
import logging
import re
from asyncio import StreamReader, StreamWriter
from logging import config
from typing import Awaitable, Callable

import websockets

from utils.state import State
import router
import settings

logger = logging.getLogger(__name__)


def sender_to_mjai(reader: StreamReader, writer: StreamWriter) -> Callable[[dict], Awaitable[dict]]:
    async def send_to_mjai(message: dict) -> dict:
        writer.write((json.dumps(message) + '\n').encode())
        await writer.drain()
        received = (await reader.readuntil()).decode()
        return json.loads(received)

    return send_to_mjai


def sender_to_tenhou(websocket, state: State) -> Callable[[dict], Awaitable[None]]:
    async def send_to_tenhou(message: dict) -> None:
        message = json.dumps(message)
        await send(websocket, message, state)

    return send_to_tenhou


async def send(websocket, message: str, state: State) -> None:
    await websocket.send(message)

    logger.debug('sent({}): {}'.format(state.name, message))


async def consumer_handler(websocket, send_to_mjai: Callable[[dict], Awaitable[dict]], state: State) -> None:
    send_to_tenhou = sender_to_tenhou(websocket, state)

    async for message in websocket:
        logger.debug('recv({}): {}'.format(state.name, message))

        try:
            message = json.loads(message)
        except json.JSONDecodeError:
            return

        for process in router.processes:
            if (await process(state, message, send_to_tenhou, send_to_mjai)):
                break

        if 'owari' in message:
            await websocket.close()


async def producer_handler(websocket, state) -> None:
    while True:
        try:
            await send(websocket, '<Z/>', state)
        except websockets.exceptions.ConnectionClosedOK:
            break

        await asyncio.sleep(10)


async def websocket_client(send_to_mjai: Callable[[dict], Awaitable[dict]], state: State) -> None:
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
        message = json.dumps({'tag': 'HELO', 'name': state.name, 'sx': settings.SEX})
        await send(websocket, message, state)
        await asyncio.gather(
            consumer_handler(websocket, send_to_mjai, state),
            producer_handler(websocket, state),
        )


async def tcp_server(reader: StreamReader, writer: StreamWriter) -> None:
    send_to_mjai = sender_to_mjai(reader, writer)
    message = await send_to_mjai({'type': 'hello', 'protocol': 'mjsonp', 'protocol_version': 3})
    name: str = message['name']
    room: str = message['room']

    if re.match(r'^(?:0|[1-7][0-9]{3})_(?:0|1|9)$', room):
        state = State(name, room)
        await websocket_client(send_to_mjai, state)
    else:
        writer.write(json.dumps({'type': 'error'}).encode())
        await writer.drain()

    writer.close()


async def main() -> None:
    server = await asyncio.start_server(tcp_server, settings.HOST, settings.PORT)

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true')
    args = parser.parse_args()

    settings.DEBUG = args.debug
    settings.LOGGING['handlers']['file']['filename'] = \
        'logs/{}.log'.format(datetime.datetime.now().strftime('%Y-%m-%d-%H%M%S'))

    config.dictConfig(settings.LOGGING)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
