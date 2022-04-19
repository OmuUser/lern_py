# Тут будет бот для дискорда
import asyncio

import discord
from discord.ext import commands
from config import settings
import json
import requests
import os, sqlite3


bot = commands.Bot(command_prefix=settings['prefix']) # Так как мы указали префикс в settings, обращаемся к словарю с ключом prefix.

# @bot.event # Эта функция позволяет отправлять сообщение в чат дискорда через консоль
# async def on_ready():
#     for i in range(1):
#         try:
#             channel = await bot.fetch_channel(input('id Канала: '))
#             await channel.send(content=input('Ваше сообщение: '))
#         except Exception:
#             print('Не хватает прав')

# @bot.event
# async def on_ready():
#     print('Bot is ready')

# @bot.event # Для отправки отложенного сообщения после включения бота
# async def task():
#     time = 10
#     await asyncio.sleep(time)
#     await bot.get_channel(964391932409311245).send('Что-то пишу, чтобы таверна не угасла )')

@bot.command()
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.

    await ctx.send(f'Привет..., {author.mention}, я готов к дальнейшим экзекуциям -_-"') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.

@bot.command()
async def pikachu(ctx): # гифка с пикачу
    response = requests.get('https://some-random-api.ml/img/pikachu') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color=0xff9900, title='Random Pikachu') # Создание Embed'a
    embed.set_image(url=json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed=embed) # Отправляем Embed

@bot.command()
async def binary(ctx, *, arg): # Эта команда переводит в двоичный код текст, если написать без звездочки, то бот уловит лишь первое слово после команды
    arg = bin(int.from_bytes(arg.encode(), 'big'))
    await ctx.send('Выводим в двоичном коде:')
    await ctx.send(arg)

@bot.command()
async def инфо(ctx, arg=None): # Инфо бота, список команд
    author = ctx.message.author
    if arg == None:
        await ctx.send(f'{author.mention} \nВведите:\n/инфо общая\n/инфо команды')
    elif arg == 'общая':
        await ctx.send(f'{author.mention} Привет! Я бот таверны, пока не многое могу, но буду развиваться ; )')
    elif arg == 'команды':
        await ctx.send(f'{author.mention} \n/pikachu - гифка с пикачу\n/binary - переведу твой текст в двоичный код (хз зачем, но вот)'
                       f'\n/hello - бот передаст персональный привет')
    else:
        await ctx.send(f'{author.mention} Нет такой команды -_-"')

# bot.loop.create_task(task()) # Для запуска таймера с отложенным сообщением
bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена

