import discord
import json
import requests
import ctypes
import asyncio
import aiohttp
import hashlib
import pystyle
import random
import os
from pystyle import * 
from discord.ext import commands 

@bot.command()
async def q(ctx):
    if not ctx.message.reference:
        await ctx.send("💬～エラーが発生しました。もう一度お試しください。")

    replymessage = await ctx.channel.fetch_message(ctx.message.reference.message_id)
    author = replymessage.author
    text = replymessage.content
    avatar_url = author.avatar.url if author.avatar else author.default_avatar.url

    url = "https://api.voids.top/quote"
    paydata = {
        "username": author.name,
        "display_name": author.display_name,
        "text": text,
        "avatar": avatar_url,
        "color": False
    }
    response = requests.post(url, json=paydata)
    data = response.json()

    print (data)

    if "url" in data:
        await ctx.send(data["url"])
    else:
        await ctx.send("❗️APIサーバーがオフラインか、タイムアウトしました。もう一度お試しください。")
        

bot.run(TOKEN)
