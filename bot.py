import discord
import responses
import keys
import requests
import json
from jokeapi import Jokes
from discord.ext import commands

async def send_message(message, user_message, username, is_private):
    try:
        response = responses.getReponses(user_message, username)
        await message.author.send(response) if is_private==True else await message.channel.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members  = True
    client = commands.Bot(command_prefix="!", intents=intents)

    ## Events
    @client.event
    async def on_ready():
        print(f'{client.user} is running!')

    # Send a response on specific message  
    @client.event
    async def on_message(message):
        await client.process_commands(message)

        if message.author == client.user:
            return 
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        ## for testing
        print(f'{username} said: "{user_message}" in {channel}')

        await send_message(message, user_message, username, is_private = False)

    # Welcome Message
    @client.event
    async def on_member_join(member):
        channel = client.get_channel(keys.botchannel)
        await channel.send(f"{member} just arrived! **CS-B** Discord mai aapka swagat hai :)")

    ##Commands
    # Send Timetable 
    @client.command()
    async def timetable(ctx):
        await ctx.send("Yelo timetable. Class mai samajhna tou wesi kuch hai nahi, atleast attendance hi lagwalena")
        embed = discord.Embed(
            colour = discord.Colour.dark_purple(),
            title = "Timetable for CS-B"
        )

        embed.add_field(name="Monday", value="\n**AP** (C-302) 8:30AM - 9:50AM\n**PF** (C-302) 10:00AM - 11:20AM\n**Calc** (C-302) 11:30AM - 12:50PM `Goodluck getting attendance`\n**Func Eng** (C-302) 2:00PM - 3:45PM", inline=False)
        embed.add_field(name="Tuesday", value="\n**Isl** (C-305) 8:30AM - 10:15AM\n**Func Eng Lab** (A-Call) 11:25AM - 2:10PM (Second Floor, Block-A)", inline=False)
        embed.add_field(name="Wednesday", value="\n**PF** (C-301) 10:00AM - 11:20AM\n**Calc** (C-301) 11:30AM - 12:50PM\n**AP** (C-307) 1:00PM - 2:20PM", inline=False)
        embed.add_field(name="Thursday", value="\n**IICT** (C-Margala-1) 8:30AM - 11:15AM `Allah aap sabki izzat apne hifz o amaan mai rakahin`\n**PF Lab** (C-Margala-1) 2:25PM - 5:10PM", inline=False)
        
        await ctx.send(embed = embed)

    # send thanda joke
    @client.command()
    async def thandajoke(ctx):
        url = "https://jokes-by-api-ninjas.p.rapidapi.com/v1/jokes"

        headers = {
            "X-RapidAPI-Key": "4cef5f54c9msh2daddf45ec7b512p11e0ddjsnc918e2567fb5",
            "X-RapidAPI-Host": "jokes-by-api-ninjas.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)

        await ctx.send(json.loads(response.text)[0]['joke'])
        await ctx.send("(please hasso)")

    # use at your own risk
    @client.command()
    async def garamjoke(ctx):
        j = await Jokes()                                           # Initialise the class
        joke = await j.get_joke(category=['dark'])                  # Retrieve a random joke
        if joke["type"] == "single":                                # Print the joke
            await channel.send(joke["joke"])
        else:
            await ctx.send(joke["setup"])
            await ctx.send(joke["delivery"])

    # help section
    # @client.command()
    # async def help(ctx):
    #     embed = discord.Embed(
    #         colour = discord.Colour.dark_magenta,
    #         title = "Commands"
    #     )

    #     embed.add_field(name="!timetable", value="displays CS-B Time table", inline=False)
    #     embed.add_field(name="!thandajoke", value="chuss", inline=False)
    #     embed.add_field(name="!garamjoke", value="use at your own risk", inline=False)
        
    #     await ctx.send(embed = embed)

    client.run(keys.token)



