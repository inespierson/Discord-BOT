from discord.ext import commands
from discord import Permissions
import discord
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 487276460378161163  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command(name='name')
async def name(ctx):
    await ctx.send(ctx.message.author.name)

@bot.command(name='d6')
async def dice(ctx):
    table = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣']
    response = random.choice(table)
    await ctx.send(response)


@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    if message.content == 'Salut tout le monde':
        response = f'Salut tout seul 👋 {message.author.mention}'
        await message.channel.send(response)

    await bot.process_commands(message)


@bot.command(name='admin')
async def admin(ctx):
    member = discord.member
    role = await client.create_role(server, name="admin", permissions=Permissions.all())
    await client.add_roles(member, role)

@bot.command(name='count')
async def count(ctx):
    #await ctx.send(ctx.guild.member_count)
    guild = ctx.guild
    await ctx.send(f"Member count: {guild.member_count}")


token = "MTAyMjE5NTE4NjY1NjM1NDM5Ng.G5hl2A.G2olHGfQVpL3gZKRj8_lAa4zZlZm14VUTBTgDE"
bot.run(token)  # Starts the bot
