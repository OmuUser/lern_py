# Тут будет бот для дискорда
import discord
from discord.ext import commands
from config import settings
import asyncio
import json
import requests


bot = commands.Bot(command_prefix=settings['prefix']) # Так как мы указали префикс в settings, обращаемся к словарю с ключом prefix.

@bot.event # Эта функция позволяет отправлять сообщение в чат дискорда через консоль
async def on_ready():
    for i in range(1):
        try:
            channel = await bot.fetch_channel(input('id Канала: '))
            await channel.send(content=input('Ваше сообщение: '))
        except Exception:
            print('Не хватает прав')

# @bot.event
# async def on_ready():
#     print('Bot is ready')

@bot.command()
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.

    await ctx.send(f'Привет!, {author.mention}!, я готов к дальнейшим экзекуциям...') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.

@bot.command()
async def pikachu(ctx):
    response = requests.get('https://some-random-api.ml/img/pikachu') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color=0xff9900, title='Random Pikachu') # Создание Embed'a
    embed.set_image(url=json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed=embed) # Отправляем Embed

bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена

