import random

def getReponses(message: str) -> str:
    pmessage = message.lower()
    text1 = 'this is so sad'
    text2 = 'mar jana chaiyan'
    text3 = 'mar jaatey hain'

    if text1 in pmessage:
        return ':ss::aa::dd:'

    if text2 in pmessage or text3 in pmessage:
        if (random.randint(1,2) == 1):
            return 'fr fr'
        else:
            return 'chalo 6th floor'

    if pmessage == 'hello':
        return 'Kia hai bey?'

    if pmessage == 'roll':
        return random.randint(1,6)

    if pmessage == '!help':
        if (random.randint(1,2) == 1):
            return '`khud samajh bhai mereko nahi maaloom`'
        else:
            return '`Theres no specific commands yet. Check back soon!`'




            
