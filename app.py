import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

from transformers import AutoProcessor, SeamlessM4Tv2Model 

processor = AutoProcessor.from_pretrained("facebook/seamless-m4t-v2-large") 
model = SeamlessM4Tv2Model.from_pretrained("facebook/seamless-m4t-v2-large")

load_dotenv()
bot_key = os.getenv("BOT_KEY")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Bot Is Ready And Online!")

@bot.event
async def on_message(message):
    if message.author.bot == False:
        if message.channel.name == 'global':
            text_inputs = processor(text=message.content, src_lang="kor", return_tensors="pt")
            output_tokens = model.generate(**text_inputs, tgt_lang="eng", generate_speech=False) 
            interpreted_message = processor.decode(output_tokens[0].tolist()[0], skip_special_tokens=True)

            await message.channel.send(interpreted_message,reference=message)
    else:
        return
    await bot.process_commands(message)

bot.run(bot_key)