import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

class DiscordBot:
    def __init__(self, bot_key, open_api_key, chat_model, prompt_template):
        self.bot_key = bot_key
        self.open_api_key = open_api_key
        self.chat_model = chat_model
        self.prompt_template = prompt_template

        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix='!', intents=intents)

        self.setup()

    def setup(self):
        @self.bot.event
        async def on_ready():
            print("Bot Is Ready And Online!")

        @self.bot.event
        async def on_message(message):
            if message.author.bot:
                return

            if message.channel.name == 'global':
                input_text = message.content
                res = self.invoke_translation_chain(input_text)
                await message.reply(res)
                
            await self.bot.process_commands(message)

    def invoke_translation_chain(self, input_text):
        prompt = ChatPromptTemplate.from_template(self.prompt_template + " {input_text}")
        model = ChatOpenAI(openai_api_key=self.open_api_key, model=self.chat_model)
        output_parser = StrOutputParser()

        chain = prompt | model | output_parser
        return chain.invoke({"input_text": input_text})

    def run(self):
        self.bot.run(self.bot_key)

if __name__ == "__main__":
    load_dotenv()
    bot_key = os.getenv("BOT_KEY")
    open_api_key = os.getenv("OPENAI_API_KEY")
    chat_model = os.getenv("CHAT_MODEL")
    prompt_template = os.getenv("PROMPT_TEMPLATE")

    bot = DiscordBot(bot_key, open_api_key, chat_model, prompt_template)
    bot.run()
