from discord.ext import commands
import win32api
from win32con import VK_MEDIA_PLAY_PAUSE, KEYEVENTF_EXTENDEDKEY, VK_MEDIA_NEXT_TRACK, VK_MEDIA_PREV_TRACK, VK_LEFT, VK_RIGHT

#set desired command prefix here
command_pfx = '!'

bot = commands.Bot(command_prefix=command_pfx)

@bot.command(name = "media", help = "Use commands playt (play toggle), next, prev, jump, or jumpb (jump back) to control host media")
async def media (ctx):
    await ctx.send("Use " + command_pfx + " with playt (play/pause), next, prev, jump, or jumpb (jump back) to control host media")

@bot.command()
async def playt(ctx):
    win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)
    await ctx.send(str(ctx.author) + " called for play/pause")

@bot.command()
async def next(ctx):
    win32api.keybd_event(VK_MEDIA_NEXT_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
    await ctx.send(str(ctx.author) + " called to go to the next media")

@bot.command()
async def prev(Ctx):
    win32api.keybd_event(VK_MEDIA_PREV_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
    await ctx.send(str(ctx.author) + " called to go to the previous media")

@bot.command()
async def jump(ctx):
    win32api.keybd_event(VK_RIGHT, 0, KEYEVENTF_EXTENDEDKEY, 0)
    await ctx.send(str(ctx.author) + " called to jump forward")

@bot.command()
async def jumpb(ctx):
    win32api.keybd_event(VK_LEFT, 0, KEYEVENTF_EXTENDEDKEY, 0)
    await ctx.send(str(ctx.author) + " called to jump back")

with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)

