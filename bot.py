import discord
import responses
from discord.ext import commands

async def send_message(message, user_message, username, is_private):
    try:
        response = responses.getReponses(user_message, username)
        await message.author.send(response) if is_private==True else await message.channel.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTE3MjA5NzAxNzMwOTMwMjgzNA.GwlgZ9.w3yr6nXrRb8YxVVc5aam-c5JHZu7RhLzYBtgG4'
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

        print(f'{username} said: "{user_message}" in {channel}')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private = True)
        else:
            await send_message(message, user_message, username, is_private = False)


    ##Commands
    
    # Send Timetable 
    @client.command()
    async def timetable(ctx):
        await ctx.send("Yelo timetable. Class mai samajhna tou wesi kuch hai nahi, atleast attendance hi lagwalena")
        embed = discord.Embed(
            #content = "Ye lo timetable. Class mai wesi kuch samajh nahi aani, atleast attendence hi lagwalo",
            colour = discord.Colour.dark_purple(),
            title = 'Timetable for CS-B'
        )

        embed.add_field(name="Monday", value="\n**AP** (C-302) 8:30AM - 9:50AM\n**PF** (C-302) 10:00AM - 11:20AM\n**Calc** (C-302) 11:30AM - 12:50PM `Goodluck getting attendance`\n**Func Eng** (C-302) 2:00PM - 3:45PM", inline=False)
        embed.add_field(name="Tuesday", value="\n**Isl** (C-305) 8:30AM - 10:15AM\n**Func Eng Lab** (A-Call) 11:25AM - 2:10PM (Second Floor, Block-A)", inline=False)
        embed.add_field(name="Wednesday", value="\n**PF** (C-301) 10:00AM - 11:20AM\n**Calc** (C-301) 11:30AM - 12:50PM\n**AP** (C-307) 1:00PM - 2:20PM", inline=False)
        embed.add_field(name="Thursday", value="\n**IICT** (C-Margala-1) 8:30AM - 11:15AM `Allah aap sabki izzat apne hifz o amaan mai rakahin`\n**PF Lab** (C-Margala-1) 2:25PM - 5:10PM", inline=False)
        
        await ctx.send(embed = embed)

    # Test Command
    @client.command()
    async def test(ctx):
        await ctx.send('done')

    client.run(TOKEN)



