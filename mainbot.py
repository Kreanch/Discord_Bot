import os
import nextcord
from nextcord.ext import commands

import cfg


intents = nextcord.Intents.all()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)


# connect
@bot.event
async def on_ready():
    game = nextcord.Game("/help")
    await bot.change_presence(status=nextcord.Status.idle, activity=game)
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


for fn in os.listdir("./cogs"):
    if fn.endswith(".py"):
        bot.load_extension(f"cogs.{fn[:-3]}")


@bot.command()
# @commands.has_permissions(administrator=True)
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    await ctx.send("Loaded cog!")


@bot.command()
# @commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    bot.unload_extension(extension)
    await ctx.send("Unloaded cog!")


@bot.command()
# @commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    bot.reload_extension(extension)
    await ctx.send("Reloaded cog!")


bot.run(cfg.TOKEN)
