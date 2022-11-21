import os
import json
import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
from pymongo import MongoClient

client = commands.Bot()
cluster = MongoClient(os.environ["DB_URL"])
playerdata = cluster["playerdata"]
GUILD_IDS = [1021559138125365280]

# Events and help command
@client.event
async def on_ready():
    print("Bot is online")

@client.slash_command(name = "help", description = "help command idk", guild_ids = GUILD_IDS)
async def help(interaction: Interaction):
    if interaction.user.id == 956278448316358666:
        desc = "hi zwei :heart_eyes:"
    else:
        desc = "idk"

    embed = nextcord.Embed(title = "Help", description = desc)
    await interaction.response.send_message(embed = embed)

@client.slash_command(name = "getplayerdata", description = "for dev", guild_ids = GUILD_IDS)
async def getplayerdata(interaction: Interaction, user: nextcord.Member):
    data = playerdata[str(user.id)]

    await interaction.response.send_message(f"{user.name} has ${data['treasury']}")

client.run(os.environ["CLIENT_TOKEN"])