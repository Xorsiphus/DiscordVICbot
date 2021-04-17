import socket
import subprocess
import sys
from discord.ext import commands
import discord

from config import TOKENS

client = commands.Bot(command_prefix='$$$')


def main():
    global client

    client.run(TOKENS['TOKEN18'])


@client.command(name='play', help='This command plays songs')
async def play(ctx):

    await ctx.message.author.voice.channel.connect(reconnect=True)

    file_name = 'ba.mp3'

    if len(sys.argv) > 2:
        channel_id = int(sys.argv[1])
        file_name = sys.argv[2]
    else:
        channel_id = 536257258695426099

    subprocess.Popen("python starter.py %d" % channel_id)

    sock = socket.socket()
    sock.bind(('127.0.0.1', 9901))
    sock.listen(1)

    conn, addr = sock.accept()

    conn.recv(2)

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('audio/' + file_name)
    voice_client.play(audio_source)


if __name__ == '__main__':
    main()
