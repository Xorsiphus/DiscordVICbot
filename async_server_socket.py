import asyncio
import socket


class ServerSocket:

    def __init__(self):
        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        self.main_loop = asyncio.new_event_loop()

    def set_up(self):
        pass

    async def accept(self):
        sock, address = await self.main_loop.sock_accept(self.socket)

    async def loop(self):
        await self.main_loop.create_task(self.accept())

    def start(self):
        self.main_loop.run_until_complete(self.loop())
