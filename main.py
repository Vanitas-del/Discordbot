import discord
from discord import app_commands
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} slash commands.')
    except Exception as e:
        print(e)

@bot.tree.command(name="log", description="Count messages by a user in #🐛brainrot-bug-reports")
@app_commands.describe(user_id="The ID of the user to search for")
async def log(interaction: discord.Interaction, user_id: str):
    await interaction.response.defer(thinking=True)

    channel = discord.utils.get(interaction.guild.text_channels, name="🐛brainrot-bug-reports")
    
    if channel is None:
        await interaction.followup.send("Channel 🐛brainrot-bug-reports not found.")
        return

    try:
        user = await interaction.guild.fetch_member(int(user_id))
    except:
        await interaction.followup.send("Invalid user ID.")
        return

    count = 0
    async for message in channel.history(limit=None):
        if message.author.id == user.id:
            count += 1

    await interaction.followup.send(f"{user.display_name} has posted **{count}** messages in {channel.mention}.")

# Run the bot
import os
bot.run(os.getenv("MTM3NzUxNDkzMjQ3OTcyNTY1MA.G7srHl.seyBporB5YncCjIGC0tAqZxgY-TnOLxh32jxgs"))
