from asyncio.windows_events import NULL
import websockets
import os

import asyncio
import json
from all_vuln_one_var import run_program


async def hello():
    await run_program()
    print("first function called")



async def echo(websocket):
    async for message in websocket:
        print(message)
        if message != NULL:
            message = message.split(" ")
        if message[0]=="start":
            rs=run_program(message[1])
        await websocket.send(json.dumps(rs))



async def main():
    async with websockets.serve(echo,  host="",
        port=int(os.environ["PORT"])):
        await asyncio.Future() 

asyncio.run(main())        