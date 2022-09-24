import asyncio
import signal
import os

import websockets
from all_vuln_one_var import run_program

async def echo(websocket):
    async for message in websocket:
        print(message)
        message=message.split(" ")
        if message[0] == "start":
            final_message = run_program(message [1])

        await websocket.send(final_message)


async def main():
    # Set the stop condition when receiving SIGTERM.
    loop = asyncio.get_running_loop()
    stop = loop.create_future()
    loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)

    async with websockets.serve(
        echo,
        host="",
        port=int(os.environ["PORT"]),
    ):
        await stop


if __name__ == "__main__":
    asyncio.run(main())