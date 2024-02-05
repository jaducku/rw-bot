import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Bot Is Ready And Online!")

@bot.event
async def on_message(message):
    if message.author.bot == False:
        if message.channel.name == '통역':
            
            await message.channel.send('통역된 말이다')
    else:
        return

bot.run('AA')