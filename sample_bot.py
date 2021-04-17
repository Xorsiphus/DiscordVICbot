import time

import discord
import sys
import os
import asyncio

from config import TOKENS

client = discord.Client()


def main(argv):
    global client

    client.run(TOKENS['TOKEN' + str(argv[1])])


# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))


async def timer(argv):
    await client.wait_until_ready()

    bot_id = int(argv[1])
    channel_id = int(argv[2])
    bots_count = float(argv[3])
    delay = float(argv[4])

    channel = client.get_channel(channel_id)

    files = os.listdir('./unicode')
    files.sort(key=lambda file: len(file))

    messages = []

    for i in range(30):
        if i % bots_count == bot_id - 1:
            f = open('./unicode/' + files[i], 'rb')
            data = '```\n' + f.read().decode('UTF-8') + '\n```'
            f.close()
            # print(data.decode('UTF-8'))
            messages.append(data)

    await asyncio.sleep(5)

    for mes in messages:
        await channel.send(mes)
        await asyncio.sleep(delay)
    await client.logout()

client.loop.create_task(timer(sys.argv))


if __name__ == '__main__':
    main(sys.argv)
