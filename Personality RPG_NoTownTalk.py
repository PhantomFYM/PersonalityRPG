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

#Enemy Check
currMonster = 1

#Attack Functions
def Attack():
    global enemyHP
    global sDisagree
    print("\nYou lunge at the monster.")
    print("The monster takes", ATK - enemyDef,"points of damage.")
    enemyHP -= (ATK - enemyDef)
    print("The monster has", enemyHP,"Health remaining.\n")
    sDisagree += 1

def TellOff():
    global enemyHP
    global disagree
    print("\nYou said some mean things to the monster.")
    print("The monster takes", ATK - enemyDef,"points of emotional damage.")
    enemyHP -= (ATK - enemyDef)
    print("The monster has", enemyHP,"Health remaining.\n")
    disagree += 1

def Discuss():
    global enemyHP
    global neutral
    print("\nYou and the monster made small talk.")
    print("The monster takes", ATK - enemyDef,"points of boredom damage.")
    enemyHP -= (ATK - enemyDef)
    print("The monster has", enemyHP,"Health remaining\n")
    neutral += 1

def Play():
    global enemyHP
    global agree
    print("\nYou decided to have fun with the monster.")
    print("The monster tires itself out, and takes", ATK - enemyDef,"points of damage.")
    enemyHP -= (ATK - enemyDef)
    print("The monster has", enemyHP,"Health remaining.\n")
    agree += 1

def Befriend():
    global enemyHP
    global sAgree
    print("\nYou tell the monster that you want to be it's good friend.")
    print("Joyfully, the monster takes", ATK - enemyDef,"points of emotional damage.")
    enemyHP -= (ATK - enemyDef)
    print("The monster has", enemyHP,"Health remaining.\n")
    sAgree += 1

def EnemyAttack():
    global enemyATK
    global Def
    global HP
    print("The monster claws into you")
    print("You take", enemyATK - Def,"damage.")
    HP -= enemyATK - Def
    print("You have",HP,"HP remaining.")
    
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
    global LVL
    global HP
    global Def
    global ATK
    if(EXP >= LVL ^ 2 + 5):
        LVL += 1
        print("You Increased in level! You are now level",LVL,"!")
        hpGain = LVL * 2 + 2
        HP += hpGain
        print("Your HP increased by",hpGain,"!")
        DefGain = LVL + 4
        Def += DefGain
        print("Your Defense increased by",DefGain,"!")
        atkGain = LVL + 2
        ATK += atkGain
        print("Your Attack increased by",atkGain,"!")

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

def BattleScreen():
    global EXP
    global currMonster
    while True:
        
        print("\n[0] Attack\n[1] Tell Off\n[2] Discuss\n[3] Play\n[4] Befriend\n")
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
            
        if(enemyHP <= 0):
            print("You slayed the monster!")
            if (currMonster == 1):
                e1Result = BattleEnd()
            elif(currMonster == 2):
                e2Result = BattleEnd()
            elif(currMonster == 3):
                e3Result = BattleEnd()
            elif(currMonster == 4):
                e4Result = BattleEnd()
            elif(currMonster == 5):
                e5Result = BattleEnd()
            elif(currMonster == 6):
                e6Result = BattleEnd()
            elif(currMonster == 7):
                e7Result = BattleEnd()
            elif(currMonster == 8):
                e8Result = BattleEnd()
            elif(currMonster == 9):
                e9Result = BattleEnd()
            elif(currMonster == 10):
                e10Result = BattleEnd()
            elif (currMonster == 11):
                e11Result = BattleEnd()
            elif(currMonster == 12):
                e12Result = BattleEnd()
            elif(currMonster == 13):
                e13Result = BattleEnd()
            elif(currMonster == 14):
                e14Result = BattleEnd()
            elif(currMonster == 15):
                e15Result = BattleEnd()
            elif(currMonster == 16):
                e16Result = BattleEnd()
            elif(currMonster == 17):
                e17Result = BattleEnd()
            elif(currMonster == 18):
                e18Result = BattleEnd()
            elif(currMonster == 19):
                e19Result = BattleEnd()
            elif(currMonster == 20):
                e20Result = BattleEnd()
            xpGain = (currMonster * 10) ^ 2
            print("You gained",xpGain,"EXP points!")
            EXP += xpGain
            lvlCheck()
            meterReset()
            currMonster += 1
            break

        EnemyAttack()

        if(HP <= 0):
            print("Game Over")
            input()
            exit()
    
#Monster functions    
def Enemy1():
    global enemyHP
    global enemyATK
    global enemyDef
    
    enemyHP = 45
    enemyATK = 20
    enemyDef = 10

#Area Menu
while True:
    print("\n[0] Town\n[1] Area\n[2] Item\n[3] Advance\n")
    townSelect = int(input())
    if(townSelect == 3):
        if (currMonster == 1):
            Enemy1()
        elif(currMonster == 2):
            Enemy2()
        elif(currMonster == 3):
            Enemy3()
        elif(currMonster == 4):
            Enemy4()
        elif(currMonster == 5):
            Enemy5()
        elif(currMonster == 6):
            Enemy6()
        elif(currMonster == 7):
            Enemy7()
        elif(currMonster == 8):
            Enemy8()
        elif(currMonster == 9):
            Enemy9()
        elif(currMonster == 10):
            Enemy10()
        elif (currMonster == 11):
            Enemy11()
        elif(currMonster == 12):
            Enemy12()
        elif(currMonster == 13):
            Enemy13()
        elif(currMonster == 14):
            Enemy14()
        elif(currMonster == 15):
            Enemy15()
        elif(currMonster == 16):
            Enemy16()
        elif(currMonster == 17):
            Enemy17()
        elif(currMonster == 18):
            Enemy18()
        elif(currMonster == 19):
            Enemy19()
        elif(currMonster == 20):
            Enemy20()
        BattleScreen()
