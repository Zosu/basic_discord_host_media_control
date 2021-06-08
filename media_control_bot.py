from discord.ext import commands
import win32api
from win32con import VK_MEDIA_PLAY_PAUSE, KEYEVENTF_EXTENDEDKEY, VK_MEDIA_NEXT_TRACK, VK_MEDIA_PREV_TRACK

bot = commands.Bot(command_prefix='!')


@bot.command(name="media", help = "Control the media that the host is streaming")
async def media(ctx, media_action: str):
    if media_action == 'playt':
        win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)
        await ctx.send("play/pause")
    elif media_action == 'next':
        win32api.keybd_event(VK_MEDIA_NEXT_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
        await ctx.send("next")
    elif media_action == 'back':
        win32api.keybd_event(VK_MEDIA_PREV_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
        await ctx.sent("back")
    else:
        await ctx.send("Unsupported input")

with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)

