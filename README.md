# Basic Discord Media Control
A very basic discord host media control bot to allow others to control the media you are streaming in a call.

# Requirements
This bot was only made to work with Windows systems. 

Use pip to install dependencies:
`pip install discord`
`pip install pywin32`

# Usage
Put media_control_bot.py into a folder along with a txt file called `BOT_TOKEN.txt` with your personalized bot token from discord, then run the program.

The default character to summon the bot is `!`.

The following commands are supported:

`!playt` for play/pause

`!next` to skip to the next media item

`!prev` to go back to the previous media item

`jump` to jump forward

`jumpb` to jump back

Note that `jump` and `jumpb` are both just mapped to the left and right arrow keys. As such, the window that the media is playing in must be in focus for these commands to function as intended. 
