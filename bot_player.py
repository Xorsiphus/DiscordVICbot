import socket
import subprocess
import sys
from discord.ext import commands
import discord

from config import TOKENS

client = commands.Bot(command_prefix='$$$')


def main():
    global client

    client.run(TOKENS['TOKEN38'])


@client.command(name='play', help='This command plays songs')
async def play(ctx):

    if ctx.message.author.id != 254600281680117760:
        return

    print('command detected!')

    if len(sys.argv) > 4:
        channel_id = int(sys.argv[1])
        file_name = sys.argv[2]  # audio file
        bots_count = int(sys.argv[3])
        video_fps = int(sys.argv[4])
    else:
        channel_id = 834021151310741527
        file_name = 'ba.mp3'
        bots_count = 37
        video_fps = 15

    subprocess.Popen("python server.py %d %d %d" % (channel_id, bots_count, video_fps))

    sock = socket.socket()
    sock.bind(('127.0.0.1', 9901))
    sock.settimeout(None)
    sock.setblocking(False)
    sock.listen(1)

    conn, addr = await client.loop.sock_accept(sock)

    await client.loop.sock_recv(conn, 2)

    await ctx.message.author.voice.channel.connect(reconnect=True)
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('audio/' + file_name)
    voice_client.play(audio_source)


if __name__ == '__main__':
    main()
