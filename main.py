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

async def fetch_collection(channel_id: int, message_id: int):
    channel = client.get_channel(channel_id)
    message = await channel.fetch_message(message_id)

    return json.loads(message.content)

async def update_collection(channel_id: int, message_id: int, new_data: str):
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

@client.slash_command(name = "dev_fetch_collection", description = "Fetch the data from the specified collection", guild_ids = GUILD_IDS)
async def dev_fetch_collection(interaction: Interaction, channelid, messageid):
    await interaction.response.send_message(f"The data loaded was `{str(await fetch_collection(int(channelid), int(messageid)))}`")

@client.slash_command(name = "dev_create_collection", description = "Create a new database collection", guild_ids = GUILD_IDS)
async def dev_create_collection(interaction: Interaction):
    await create_collection(1035428713963208734, {"this is an empty collection": "", "use the /dev_update_collection command to update the data": ""})
    await interaction.response.send_message(f":white_check_mark: Collection created")

@client.slash_command(name = "dev_update_collection", description = "ee", guild_ids = GUILD_IDS)
async def dev_update_collection(interaction: Interaction, channelid, messageid, data: str):
    await update_collection(int(channelid), int(messageid), data)
    await interaction.response.send_message(f":white_check_mark: Collection updated. Jump: https://discord.com/channels/1021559138125365280/{channelid}/{messageid}")

client.run(os.environ["CLIENT_TOKEN"])