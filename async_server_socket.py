import asyncio
import socket


class ServerSocket:

    def __init__(self):
        self.sockets = []
        self.connections = []
        self.main_loop = asyncio.new_event_loop()

    def set_up(self, i):
        cur_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        cur_socket.bind(('127.0.0.1', 9902 + i))
        cur_socket.listen(1)
        cur_socket.setblocking(False)
        self.sockets.append(cur_socket)

    async def accept(self, i):
        sock, address = await self.main_loop.sock_accept(self.sockets[i])
        self.connections.append(sock)

    async def send(self, i, mes):
        await self.main_loop.sock_sendall(self.sockets[i], mes.encode('UTF-8'))

    # async def loop(self):
    #
    #     await self.main_loop.create_task(self.accept())
    #
    # def start(self):
    #     self.main_loop.run_until_complete(self.loop())
