#Attack Functions
def Attack():
    global enemyHP
    global sDisagree
    print()
    print("You lunge at the monster.")
    print("The monster takes", ATK - enemyDef,"points of damage.")
    enemyHP -= (ATK - enemyDef)
    print("The monster has", enemyHP,"Health remaining.")
    print()
    sDisagree += 1

def TellOff():
    global enemyHP
    global disagree
    print()
    print("You said some mean things to the monster.")
    print("The monster takes", ATK - enemyDef,"points of emotional damage.")
    enemyHP -= (ATK - enemyDef)
    print("The monster has", enemyHP,"Health remaining.")
    print()
    disagree += 1

def Discuss():
    global enemyHP
    global neutral
    print()
    print("You and the monster made small talk.")
    print("The monster takes", ATK - enemyDef,"points of boredom damage.")
    enemyHP -= (ATK - enemyDef)
    print("The monster has", enemyHP,"Health remaining")
    print()
    neutral += 1

def Play():
    global enemyHP
    global agree
    print()
    print("You decided to have fun with the monster.")
    print("The monster tires itself out, and takes", ATK - enemyDef,"points of damage.")
    enemyHP -= (ATK - enemyDef)
    print("The monster has", enemyHP,"Health remaining.")
    print()
    agree += 1

def Befriend():
    global enemyHP
    global sAgree
    print()
    print("You tell the monster that you want to be it's good friend.")
    print("Joyfully, the monster takes", ATK - enemyDef,"points of emotional damage.")
    enemyHP -= (ATK - enemyDef)
    print("The monster has", enemyHP,"Health remaining.")
    print()
    sAgree += 1







    

#Checking and Battle functions
def BattleEnd(currentEnemy= 2):
    global sDisagree
    global disagree
    global neutral
    global agree
    global sAgree
    meter = sDisagree, disagree, neutral, agree, sAgree
    currentEnemy = meter.index(max(meter))
    return currentEnemy

def lvlCheck():
    if(EXP == LVL ^ 2 + 5):
        LVL += 1
        HP += LVL * 2 + 2
        Def += LVL + 4
        ATK += LVL + 2

def meterReset():
    global sDisagree
    global disagree
    global neutral
    global agree
    global sAgree
    sDisagree = 0
    disagree = 0
    neutral = 0
    agree = 0
    sAgree = 0
    

    

#Monster functions    
def Enemy1():
    global enemyHP
    global enemyATK
    global enemyDef
    
    enemyHP = 5
    enemyATK = 2
    enemyDef = 3

#Default Stats
EXP = 0
LVL = 1
HP = 10
Def = 0
ATK = 5

#Default Enemy Stats
enemyHP = 0
enemyDef = 0
enemyATK = 0

#Agreement Meters
sDisagree = 0
disagree = 0
neutral = 0
agree = 0
sAgree = 0
meter = ()


#Combat trial

Enemy1()


while True:
    if(enemyHP <= 0):
        print("You slayed the monster!")
        e1Result = BattleEnd()
        lvlCheck()
        meterReset()
        break
    
    print("[0] Attack\n[1] Tell Off\n[2] Discuss\n[3] Play\n[4] Befriend\n")
    select = int(input())
    if(select == 0):
        Attack()
    elif(select == 1):
        TellOff()
    elif(select == 2):
        Discuss()
    elif(select == 3):
        Play()
    elif(select == 4):
        Befriend()
