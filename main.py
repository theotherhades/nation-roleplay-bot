import os
import json
import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import commands

client = commands.Bot()
GUILD_IDS = [1021559138125365280]

# Database functions
def fetch_data(channel_id: int, message_id: int):
    channel = client.get_channel(channel_id)
    message = channel.fetch_message(message_id)
    return json.loads(message.content)

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
    await interaction.response.send_message(f"the data loaded was `{str(fetch_data(1035428713963208734, 1035428847581134931))}`")

client.run(os.environ["CLIENT_TOKEN"])