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

#Boss monster stats
monStatMap = {
1: (45, 0, 0), #Enemy1
2: (45, 0, 0), #Enemy2
3: (45, 0, 0), #Enemy3
4: (45, 0, 0), #Enemy4
5: (45, 0, 0), #Enemy5
}

miniMonStatMap = {
1: (10, 0, 0),
2: (10, 0, 0),
3: (10, 0, 0),
4: (10, 0, 0),
5: (10, 0, 0),
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
"john": "Good job you made it to the next town",
"percy": "wow thats impressive",
"jewel": "intresting"
},
3: {
"mark": "oh you think you accomplished something",
"cleo": "how strange",
"sam": "you have a long way to go"
},
4: {
"dean": "wow",
"emily": "if you want to know more keep going",
"susan": "so how was the monsters"
},
5: {
"lily": "well well",
"joseph": "Test words 2",
"steve": "Test words 3"
},
6: {
"jessie": "Test words 1",
"rick": "Test words 2",
"daryl": "Test words 3"
},
7:{
"steveee": "Test words 1",
"test2": "Test words 2",
"sophia": "Test words 3"
},
8:{
"amy": "Test words 1",
"holt": "Test words 2",
"charles": "Test words 3"
},
9:{
"michonne": "Test words 1",
"carl": "Test words 2",
"negan": "Test words 3"
},
10:{
"sony": "Test words 1",
"apple": "Test words 2",
"pear": "Test words 3"
},
11:{
"ceaser": "Test words 1",
"salad": "Test words 2",
"ranch": "Test words 3"
},
12:{
"pizza": "Test words 1",
"cheese": "Test words 2",
"milk": "Test words 3"
},
13:{
"m": "Test words 1",
"s": "Test words 2",
"t": "Test words 3"
},
14:{
"hi": "Test words 1",
"hello": "Test words 2",
"eee": "Test words 3"
},
15:{
"test": "Test words 1",
"test": "Test words 2",
"test": "Test words 3"
},
16:{
"test": "Test words 1",
"test": "Test words 2",
"test": "Test words 3"
},
17:{
"test": "Test words 1",
"test": "Test words 2",
"test": "Test words 3"
},
18:{
"test": "Test words 1",
"test": "Test words 2",
"test": "Test words 3"
},
19:{
"test": "Test words 1",
"test": "Test words 2",
"test": "Test words 3"
},
20:{
"test": "Test words 1",
"test": "Test words 2",
"test": "Test words 3"
},
}
    
#Town Functions
def town(currTown):
    while True:
        print(f"\nWelcome to Town {currTown}\n")
        for person, message in towns[currTown].items():
            print(f"[{person}] {message}")
        break
    if (3<=0):
        print(f"\nWelcome to Town {currTown}\n")
    else:
        print("\nTo get to next town you gave to beat the next boss")
        





#Attack Functions


def miniAttack():
    print("\nYou lunge at the small monster.")
    print("The monster takes", stats["ATK"] - monStats["Def"],"points of damage.")
    monStats["HP"] -= (stats["ATK"] - monStats["Def"])
    print("The monster has", monStats["HP"],"Health remaining.\n")
    
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
        stats["EXP"] = 0
        stats["LVL"] += 1
        print("You Increased in level! You are now level",stats["LVL"],"!")
    
        hpGain = stats["LVL"] * 2 + 2
        stats["HP"] += hpGain
        print("Your HP increased by",hpGain,"!")
        defGain = stats["LVL"] + 4
        stats["Def"] += defGain
        print("Your Defense increased by",defGain,"!")
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
                #if-statements.
                
            xpGain = (currMonster * 10) ^ 2
            print("You gained",xpGain,"EXP points!\n")
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

def miniBattleScreen():
    while True:
        
        select = input("\n[0] Attack\n[1] Run\n\n")
        if (select.isdigit()): #Tests if select is a digit input before confirming
            select = int(select)
            if(select == 0):
                miniAttack()
                
            elif(select == 1):
                print("\nYou ran away.\n")
                break
            
            else:
                print("\nInvalid Input, try again.")
            
        else:
            print("\nInvalid Input, try again.")
            
        if(monStats["HP"] <= 0):
            print("You slayed the small monster!")
            xpGain = (currMonster * 2)
            print("You gained",xpGain,"EXP points!")
            stats["EXP"] += xpGain
            lvlCheck()
            miniSelect = input("Continue in field? \n[0] Yes\n[1] No\n")
            if(miniSelect.isdigit()):
                miniSelect = int(miniSelect)
                if(miniSelect == 0):
                    setMonStats(*miniMonStatMap.get(currMonster, (0, 0, 0)))
                    continue
                if(miniSelect == 1):
                    break
                    
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
    print("\n[0] Town\n[1] Area\n[2] Item\n[3] Advance\n[4] Stats\n")
    townSelect =(input())
    if(townSelect.isdigit()):
        townSelect = int(townSelect)

        if(townSelect == 0):
            town(currMonster)
            continue

        if(townSelect == 1):
            setMonStats(*miniMonStatMap.get(currMonster, (0, 0, 0)))
            miniBattleScreen()
            continue
            
        if(townSelect == 3):
            setMonStats(*monStatMap.get(currMonster, (0, 0, 0))) #Unpacks and repacks tuple, as well as record enemy stats.
            BattleScreen()
            continue

        if(townSelect == 4):
            print(stats)
                
        else:
            print("\nInvalid Input, try again.")
        
    else:
        print("\nInvalid Input, try again.")
        

#Personality Statements
if(e1Result == 0 and e2Result == 1 and e3Result == 2 and e4Result == 3 and e5Result == 4):
                print("Your personality is INTJ, imaginative and stragetic thinkers with a plan for everything.")

if(e1Result == 0 and e2Result == 1 and e3Result == 2 and e4Result == 3 and e5Result == 4):
                    print("Your personality is INTP, innovative investors with a lot of knowledge.")

if(e1Result == 0 and e2Result == 1 and e3Result == 2 and e4Result == 3 and e5Result == 4):
                print("Your personality is ENTJ, bold, imaginative and strong-willed leaders, always finding a way- or making one.") 

if(e1Result == 0 and e2Result == 1 and e3Result == 2 and e4Result == 3 and e5Result == 4):
                print("Your personality is ENTP, smart and curious thinkers who ca not resist an intellectual challenge.")

if(e1Result == 0 and e2Result == 1 and e3Result == 2 and e4Result == 3 and e5Result == 4):
                print("Your personality is INFJ, quiet and mystical, yet very inpiring and tireless idealist.") 

if(e1Result == 0 and e2Result == 1 and e3Result == 2 and e4Result == 3 and e5Result == 4):
                print("Your personality is INFP, poetic, kind and altruistic people, always eager to help a good cause.") 

if(e1Result == 0 and e2Result == 1 and e3Result == 2 and e4Result == 3 and e5Result == 4):
                print("Your personality is ENFJ, charamasitc and inspiring leaders able to mesmerize their listeners.") 

if(e1Result == 0 and e2Result == 1 and e3Result == 2 and e4Result == 3 and e5Result == 4):
                print("Your personality is ENFP, euthusiastic, creative and socialable free spirits, who can always find a reason to smile.")

if(e1Result == 0 and e2Result == 1 and e3Result == 2 and e4Result == 3 and e5Result == 4):
                print("Your personality is ISTJ, practical and fact-minded individuals, whose reliability can not be doubled.") 

if(e1Result == 0 and e2Result == 1 and e3Result == 2 and e4Result == 3 and e5Result == 4):
                print("Your personality is ISFJ, very dedicated and warm protectors, always ready to defend their loved ones.") 

if(e1Result == 0 and e2Result == 1 and e3Result == 2 and e4Result == 3 and e5Result == 4):
                print("Your personality is ESTJ, excellent administrators, unsurpassed at managing things or people.")  

if(e1Result == 0 and e2Result == 1 and e3Result == 2 and e4Result == 3 and e5Result == 4):
                print("Your personality is ESFJ, caring, social, and popular people, always eager to help.") 

if(e1Result == 0 and e2Result == 1 and e3Result == 2 and e4Result == 3 and e5Result == 4):
                print("Your personality is ISTP, bold and practical experimenters") 

if(e1Result == 0 and e2Result == 1 and e3Result == 2 and e4Result == 3 and e5Result == 4):
                print("Your personality is ISFP, flexible and charming artists always ready to explore and experience something new.")
                
if(e1Result == 0 and e2Result == 1 and e3Result == 2 and e4Result == 3 and e5Result == 4):
                print("Your personality is ESTP, smart, energentic and very  perceptive people.") 

if(e1Result == 0 and e2Result == 1 and e3Result == 2 and e4Result == 3 and e5Result == 4):
                print("Your perosnality is ESFP, spontaneous, energetic and enthusiastic people.")
        
else:
        print("\nInvalid Input, try again.")
