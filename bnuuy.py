import discord
import random
from discord.ext import commands

bot_token = 'ENTER__BOT_TOKEN_HERE_PLEASE_<3'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'bnuuy gamer mode activated')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'bnuuy' in message.content.lower():
        emoji = random.choice(['👀', '🐸', '🍌', '🎉', '🌟', '🔥', '👍', '😀'])
        response = f'bnuuy {emoji}'
        await message.channel.send(response)
    
    await bot.process_commands(message)

bot.run(bot_token)
