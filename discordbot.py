import discord
import asyncio
from discord.ext import commands
import math
from discord.ext.commands.cooldowns import BucketType
from discord.ext.commands import Bot

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

bot = commands.Bot(command_prefix='m!', description=description)

@bot.command()
async def hi():
    """responds with a inside joke"""
    await bot.say("https://www.youtube.com/watch?v=BfoR8SbFhy8")

	
@bot.command()
@commands.cooldown(1, 10, BucketType.user)
async def add(left : int, right : int):
        """Adds two numbers together."""
        await bot.say(left + right)
        await bot.say("Wait 10 seconds to use it again")

@bot.command()
@commands.cooldown(1, 10, BucketType.user)
async def divide(left : int, right : int) :
        """devides to numbers"""
        await bot.say(left / right)
        await bot.say("Wait 10 seconds to use it again")

@bot.command()
@commands.cooldown(1, 10, BucketType.user)
async def multiply(left : int, right : int) :
    """multiplayers from left to right"""
    await bot.say(left * right)
    await bot.say("Wait 10 seconds to use it again")

@bot.event
async def on_ready():

    await bot.change_presence(game=discord.Game(name='Use m!help'))

@bot.event
async def on_server_join(server):
        await bot.send_message(server.default_channel, """Hello people of this server! I am Calculon Bot (Prev known as Calculon 2.0) I will be assisting you with your discord bot needs! To see the list of commands, feel free to use ```m!help``` and to see my music commands please use ```m!musichelp```. To join our support server please click this discord link: https://discord.gg/Azqkpze. Thanks again for adding me here!""")

@bot.command()
async def doomfist():
    """links to doomfist video"""
    await bot.say("https://www.youtube.com/watch?v=vaZfZFNuOpI")

@bot.command()
@commands.cooldown(1, 10, BucketType.user)
async def subtract(left : int, right : int) :
         """Subtracts numbers from left to right"""
         await bot.say(left - right)
         await bot.say("Wait 10 seconds to use it again")

@bot.command()
@commands.cooldown(1, 30, BucketType.user)
async def ping():
    """Pong!"""
    await bot.say("Pong!")
    await bot.say("Wait 10 seconds to use it again")

@bot.command()
async def echo(*args):
    """echos what you say"""
    string = " ".join(args)
    return await bot.say(string)
	
@bot.command()
@commands.cooldown(1, 10, BucketType.user)
async def squareroot(x):
    """finds the squareroot"""
    if x.isdigit():
        await bot.say(math.sqrt(int(x)))
    else:
        await bot.say("Please insert numbers only :pray:")
    await bot.say("Wait 10 seconds to use it again")
		
@bot.command()
@commands.cooldown(1, 10, BucketType.user)
async def exponent(left : int, right : int) :
        """left to the power of right"""
        await bot.say(left ** right)
        await bot.say("Wait 10 seconds to use it again")

@bot.command()
@commands.cooldown(1, 10, BucketType.user)
async def mpi(user):
        if user.isdiit():
            return await bot.say(math.pi * (int(user)))
        else:
            await bot.say("Please insert numbers only :pray:")
        await bot.say("Wait 10 seconds to use it again")


@bot.command()
async def pi():
    """what pi is equal to"""
    return await bot.say("""Pi is equal to:
    3.14159265359""")

@bot.command()
async def trivia(answer):
    """To use the trivia, please start with !trivia one, to get the first questions"""
    if answer == "one":
        return await bot.say("""Who made the equation e = mc2?
        [A]Michael Jackson
        [B]Isaac Newton
        [C]Albert Einstein
        [D]Jeff Kaplan
        use !trivia (letter) to choose your answer""")
    if answer == "A":
        await bot.say("Wrong! use !trivia 1 to try again!")
    if answer == "B":
        await bot.say("Wrong! use !trivia 1 to try again!")
    if answer == "C":
        await bot.say("Correct!")
    if answer == "D":
        await bot.say("Wrong! use !trivia 1 to try again!")

@bot.command()
async def github():
    """Displays the github page for Mebot"""
    await bot.say("""Calculon is a open source bot! The github page is
    https://github.com/Memewotic/CalculonBot""")

@bot.command()
async def credit():
    """Displays the bot creators"""
    await bot.say("""Mebot was created by a group of people, including:
    Memewotic = Founder/Developer
    Michel = Emotional Support
    Nightmare = Ideas/Bug finder
    Discord.Py for making this project possible
    And the people over at:
    https://github.com/Just-Some-Bots/MusicBot
    for making me able to do music function!
massive thanks to these people!""")

@bot.command()
async def hack():
    """hacks the entire internet for you, kinda..."""
    await bot.say("https://giphy.com/embed/YQitE4YNQNahy")

@bot.command(pass_context = True)
@commands.cooldown(1, 10, BucketType.user)
async def clear(ctx, number):
    """Clear specified msgs. BOT HAS TO BAVE PERMISSION TO DELETE"""
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await bot.delete_messages(mgs)
    await bot.say("Wait 10 seconds to use it again")
	
@bot.command()
async def musichelp():
    """**DISPLAYS COMMANDS FOR THE MUSIC FUNCTION OF CALCULON BOT**"""
    await bot.say("""Commands are ```m!musichelp, m!play, m!np, m!skip, m!search, m!shuffle, m!clear, m!pause, m!resume, m!summon, m!disconnect```
    **TO CHECK OUT DETAILED COMMANDS FOR CALCULON BOT (MUSIC SECTION) PLEASE GO TO**:
    https://github.com/Memewotic/CalculonBot/wiki/Music-Commands :thumbsup:""")
bot.run(token)
