from discord.ext import commands
import discord
import sys

from config import TOKENS

# client = discord.Client()
client = commands.Bot(command_prefix='$$$')


def main():
    global client

    client.run(TOKENS['TOKEN18'])


@client.command(name='play', help='This command plays songs')
async def play(ctx):

    server = ctx.message.guild
    voice_channel = server.voice_client

    await ctx.message.author.voice.channel.connect(reconnect=True)
    await voice_channel.play(discord.FFmpegPCMAudio('audio/ba.mp3'), None)
    voice_channel.stop()


if __name__ == '__main__':
    main()
