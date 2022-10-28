import os
import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import commands

client = commands.Bot()
GUILD_IDS = [1021559138125365280]

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

client.run(os.environ["CLIENT_TOKEN"])