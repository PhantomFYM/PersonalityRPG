#Default Stats
stats = {
"EXP": 0,
"LVL": 1,
"HP": 10,
"Def": 0,
"ATK": 5,
}

#Default Enemy Stats
monStats = {
"HP": 0,
"Def": 0,
"ATK": 0,
}

#Agreement Meters
meters = {
"sDisagree": 0,
"disagree": 0,
"neutral": 0,
"agree": 0,
"sAgree": 0,
}

#Enemy Check
currMonster = 1

#BattleResults
eResults = {}

#Town texts
towns = {
    1: {
        "Bob": "Hello Traveler! Here is info.",
        "Louis": "Hello, be careful there are monsters around.",
        "Sarah": "What's up."
        },
    2: {
        "Test1": "Test words 1",
        "Test2": "Test words 2",
        "Test3": "Test words 3"
        },
    }
    
#Town Functions
def town(currTown):
    while True:
        print(f"\nWelcome to Town {currTown}\n")
        for person, message in towns[currTown].items():
            print(f"[{person}] {message}")
        break
            
#Attack Functions
def Attack():
    print("\nYou lunge at the monster.")
    print("The monster takes", stats["ATK"] - monStats["Def"],"points of damage.")
    monStats["HP"] -= (stats["ATK"] - monStats["Def"])
    print("The monster has", monStats["HP"],"Health remaining.\n")
    meters["sDisagree"] += 1

def TellOff():
    print("\nYou said some mean things to the monster.")
    print("The monster takes", stats["ATK"] - monStats["Def"],"points of emotional damage.")
    monStats["HP"] -= (stats["ATK"] - monStats["Def"])
    print("The monster has", monStats["HP"],"Health remaining.\n")
    meters["disagree"] += 1

def Discuss():
    print("\nYou and the monster made small talk.")
    print("The monster takes", stats["ATK"] - monStats["Def"],"points of boredom damage.")
    monStats["HP"] -= (stats["ATK"] - monStats["Def"])
    print("The monster has", monStats["HP"],"Health remaining\n")
    meters["neutral"] += 1

def Play():
    print("\nYou decided to have fun with the monster.")
    print("The monster tires itself out, and takes", stats["ATK"] - monStats["Def"],"points of damage.")
    monStats["HP"] -= (stats["ATK"] - monStats["Def"])
    print("The monster has", monStats["HP"],"Health remaining.\n")
    meters["agree"] += 1

def Befriend():
    print("\nYou tell the monster that you want to be it's good friend.")
    print("Joyfully, the monster takes", stats["ATK"] - monStats["Def"],"points of emotional damage.")
    monStats["HP"] -= (stats["ATK"] - monStats["Def"])
    print("The monster has", monStats["HP"],"Health remaining.\n")
    meters["sAgree"] += 1

def EnemyAttack():
    print("The monster claws into you")
    print("You take", monStats["ATK"] - stats["Def"],"damage.")
    stats["HP"] -= monStats["ATK"] - stats["Def"]
    print("You have",stats["HP"],"HP remaining.")
    
#Checking and Battle functions
def BattleEnd(currentEnemy= 2):
    currentEnemy = max(meters)
    return currentEnemy

def lvlCheck():
    if(stats["EXP"] >= stats["LVL"] ^ 2 + 5):
        LVL += 1
        print("You Increased in level! You are now level",stats["LVL"],"!")
        hpGain = stats["LVL"] * 2 + 2
        stats["HP"] += hpGain
        print("Your HP increased by",hpGain,"!")
        DefGain = LVL + 4
        stats["Def"] += DefGain
        print("Your Defense increased by",DefGain,"!")
        atkGain = stats["LVL"] + 2
        stats["ATK"] += atkGain
        print("Your Attack increased by",atkGain,"!")

def meterReset():
    for value in meters: #Resets all values in meter, preparing for next monster
        meters[value] = 0

def BattleScreen():
    global currMonster
    while True:
        
        select = input("\n[0] Attack\n[1] Tell Off\n[2] Discuss\n[3] Play\n[4] Befriend\n")
        if (select.isdigit()): #Tests if select is a digit input before confirming
            select = int(select)
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
            else:
                print("\nInvalid Input, try again.")
            
        else:
            print("\nInvalid Input, try again.")
            
        if(monStats["HP"] <= 0):
            print("You slayed the monster!")
            
            if (1 >= currMonster <= 20):
                eResults[f"e{currMonster}Result"] = BattleEnd() #f-string used to call a variable in the string, drastically shrinks
                #if-statements. Thanks again python discord.
                
            xpGain = (currMonster * 10) ^ 2
            print("You gained",xpGain,"EXP points!")
            stats["EXP"] += xpGain
            lvlCheck()
            meterReset()
            currMonster += 1
            break

        EnemyAttack()

        if(stats["HP"] <= 0):
            print("Game Over")
            input()
            exit()
    
#Monster functions    
def setMonStats(HP, ATK, Def):
    global monStats
    monStats = {
        "HP": HP,
        "ATK": ATK,
        "Def": Def,
        }

#Area Menu
while True:
    print("\n[0] Town\n[1] Area\n[2] Item\n[3] Advance\n")
    townSelect =(input())
    if(townSelect.isdigit()):
        townSelect = int(townSelect)
        if(townSelect == 0):
            town(currMonster)
            continue
            
        if(townSelect == 3):
            monStatMap = {
                1: (45, 0, 0), #Enemy1
                }
            setMonStats(*monStatMap.get(currMonster, (0, 0, 0))) #Unpacks and repacks tuple, as well as record enemy stats.
            BattleScreen()
            continue
                
        else:
            print("\nInvalid Input, try again.")
        
    else:
        print("\nInvalid Input, try again.")
