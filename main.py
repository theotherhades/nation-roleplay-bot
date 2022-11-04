import os
import json
import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import commands

client = commands.Bot()
GUILD_IDS = [1021559138125365280]

# Database functions
async def create_collection(channel_id: int, data: dict):
    channel = client.get_channel(channel_id)

    await channel.send(json.dumps(data))

async def fetch_data(channel_id: int, message_id: int):
    channel = client.get_channel(channel_id)
    message = await channel.fetch_message(message_id)

    return json.loads(message.content)

async def update_data(channel_id: int, message_id: int, new_data: str):
    channel = client.get_channel(channel_id)
    message = await channel.fetch_message(message_id)
    
    await message.edit(new_data)

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

@client.slash_command(name = "test", description = "test", guild_ids = GUILD_IDS)
async def test(interaction: Interaction):
    await interaction.response.send_message(f"the data loaded was `{str(await fetch_data(1035428713963208734, 1035428847581134931))}`")

@client.slash_command(name = "collection_test", description = "[testing] create a new database collection", guild_ids = GUILD_IDS)
async def collection_test(interaction: Interaction):
    await create_collection(1035428713963208734, {"zwei is": "incrediby hot", "ramen is": "hot as well"})
    await interaction.response.send_message("balls")

@client.slash_command(name = "update_collection", description = "ee", guild_ids = GUILD_IDS)
async def update_collection(interaction: Interaction, data: str, channelid: int, messageid: int):
    await update_data(channelid, messageid, data)
    await interaction.response.send_message(f":thumbsup: Collection updated. Jump: https://discord.com/1021559138125365280/{channelid}/{messageid}")

client.run(os.environ["CLIENT_TOKEN"])