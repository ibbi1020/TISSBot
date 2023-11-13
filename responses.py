import random

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
    if pmessage == '!help':
        if (random.randint(1,2) == 1):
            return '`khud samajh bhai mereko nahi maaloom`'
        else:
            return '`Theres no specific commands yet. Check back soon!`'
    
    ## Rehan Bully section
    if username == 'rehanakram':
        if (random.randint(1, 20)==1):
            return 'jhoot!'

    ## Sagar Bully Section
    if username == 'Ragas#7132':
        if (random.randint(1, 10) == 1):
            return 'Sagar shanakhti card ban gaya ya abhi bhi minor ho?'

    ## kaam ki cheezain:
    # Timetable: 
    timetable = "`Monday:\n\tAP (C-302) [8:30AM - 9:50AM]\n\t(C-302) [10:00AM - 11:20AM]\n\tCalc (C-302) [11:30AM - 12:50PM]\n\tFunc Eng (C-302) [2:00PM - 3:45PM]\n\nTuesday:\n\tIsl (C-305) [8:30AM - 10:15AM]\n\tFunc Eng Lab (A-Call) [11:25AM - 2:10PM] (Second Floor, Block-A)\n\nWednesday:\n\tPF (C-301) [10:00AM - 11:20AM]\n\tCalc (C-301) [11:30AM - 12:50PM]\n\tAP (C-307) [1:00PM - 2:20PM]\n\nThursday:\n\tIICT (C-Margala-1) [8:30AM - 11:15AM] Allah aap sabko apne hifz o amaan mai rakahin\n\tPF Lab (C-Margala-1) [2:25PM - 5:10PM]`\n"
    if pmessage == '!timetable':
        if (random.randint(1,3)==1):
            return 'sab kaam mai khud karoon?'
        return timetable