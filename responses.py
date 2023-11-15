import random
import discord
import responses
import discord.ext

def getReponses(message: str, username) -> str:
    pmessage = message.lower()
    text1 = 'this is so sad'
    text2 = 'mar jana chaiyan'
    text3 = 'mar jaatey hain'

    if text1 in pmessage:
        return '<:ss:1169124467600015360><:aa:1169124417582940170><:dd:1169124140620468284>'

    ## Chawal i guess idk honestly 
    if text2 in pmessage or text3 in pmessage or pmessage == 'kms':
        if (random.randint(1,2) == 1):
            return 'fr fr'
        else:
            return 'chalo 6th floor'
    
    ## Rude hello
    if pmessage == 'hello' or pmessage == 'hi':
        return 'Kia hai bey?'

    if pmessage == 'roll':
        return random.randint(1,6)

    ## Unhelpful help 
    # if pmessage == '!help':
    #     if (random.randint(1,2) == 1):
    #         return '`khud samajh bhai mereko nahi maaloom`'
    #     else:
    #         return '`**!timetable** - CS-B Time Table\n**!thandajoke** - chuss\n**!garamjoke** - use at your own risk`'
    
    ## Rehan Bully section
    if username == 'rehanakram':
        if (random.randint(1, 20)==1):
            return 'jhoot!'

    ## Sagar Bully Section
    if username == 'Ragas#7132':
        if (random.randint(1, 10) == 1):
            return 'Sagar shanakhti card ban gaya ya abhi bhi minor ho?'

    ## kaam ki cheezain:
    