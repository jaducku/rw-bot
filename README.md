# <p align="center">Interpreter Bot</p>

## Description
A discord bot that translates every language.
- Korean -> English
- Others -> Korean

# Language
Python 3.9

## Dependency
```bash
$ pip python-dotenv 
$ pip discord.py
$ pip langchain
$ pip langchain-core
$ pip langchain-community
$ pip langchain-community
$ pip langchain-openai
```

## Setup
- Step 1. make .env in root directory
- Step 2. Add 4 Env Values
```text
BOT_KEY={discord bot api key}
OPENAI_API_KEY={open api key}
CHAT_MODEL={chat model on open api}
PROMPT_TEMPLATE={prompt template}
```

## Advice
- **The prompt should clearly state what to do and what not to do**
- **You have to write a prompt so that bot doesn't listen to other commands**

## Running the app
```bash
python bot.py
```

## Support
jaducku@gmail.com

## License
[MIT licensed](LICENSE).
