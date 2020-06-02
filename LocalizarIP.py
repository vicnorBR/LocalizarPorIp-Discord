import requests
import socket
import discord
from discord.ext import commands
from discord.ext.commands import Bot

c = requests.session()

def GeoIP(IP):
    response = socket.gethostbyname(IP.replace(" ",""))
    Link = "http://api.db-ip.com/v2/free/{0}".format(response).replace(" ","")
    c.headers.update({"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.129"})
    c.headers.update({"content-type":"text/html; charset=UTF-8"})
    x = c.get(Link)
    IP = str(x.content).replace("\\u00e7","ç").replace("\\u00e3","ã").split('"ipAddress": "')[1].split('"')[0]
    Continente = str(x.content).replace("\\u00e7","ç").replace("\\u00e3","ã").split('"continentName": "')[1].split('"')[0]
    Pais = str(x.content).replace("\\u00e7","ç").replace("\\u00e3","ã").split('"countryName": "')[1].split('"')[0]
    Estado = str(x.content).replace("\\u00e7","ç").replace("\\u00e3","ã").split('"stateProv": "')[1].split('"')[0]
    Cidade = str(x.content).replace("\\u00e7","ç").replace("\\u00e3","ã").split('"city": "')[1].split('"')[0]
    return "```md\n[IP]("+IP.replace("\\","")+")\n[Continente]("+Continente.replace("\\","")+")\n[Pais]("+Pais.replace("\\","")+")\n[Estado]("+Estado.replace("\\","")+")\n[Cidade]("+Cidade.replace("\\","")+")\n```"

client = discord.Client()

@client.event
async def on_message(message):
    if(message.author.id == SeuID):
        if(message.content.split(" ")[0] == "*localizar"):
            await message.channel.send(GeoIP(message.content.split("*localizar")[1]))

client.run("SeuToken",bot=False)
