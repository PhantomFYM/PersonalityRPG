def intro():
    print("\n\n--------Coma--------")
    print("In the eerie depths of the coma, they found themselves ensnared within the tangled maze of their")
    print("own mind, where memories morphed into grotesque shapes and nightmares loomed in every")
    print("shadow. Each night, as consciousness slipped deeper into oblivion, they were ensnared by visions")
    print("of their past, twisted and distorted by the darkness that lurked within.\n")

    print("In their dreams, they wandered through a desolate wasteland, where the once verdant meadows of")
    print("childhood lay barren and lifeless. The wildflowers had withered into twisted thorns that tore at their")
    print("flesh, drawing blood with every step. The warmth of a mother's embrace had turned into a")
    print("suffocating grip, drowning them in a sea of guilt and regret.\n")

    print("Amidst the chaos, there were echoes of laughter—a cruel mockery of the joy they once knew. These")
    print("echoes taunted them, reminding them of the happiness they could never reclaim, the moments")
    print("lost to the void of the coma.\n")

    print("But amidst the despair, there was a glimmer of hope—a memory buried beneath the layers of pain")
    print("and darkness. It was a dull memory of love, tainted by betrayal and heartache, yet still burning with")
    print("a flicker of warmth. This ambiguous love became their lifeline, guiding them through the labyrinth of")
    print("nightmares, a beacon of light in the suffocating darkness.\n")

    print("As the days blurred into weeks and the weeks into months, they teetered on the brink of madness,")
    print("grappling with the demons that lurked within their own mind. Yet even in the darkest depths of the")
    print("coma, there remained a sliver of humanity—a spark of resilience that refused to be extinguished.\n")

    print("And so, they clung to that spark with every ounce of strength they possessed, knowing that within")
    print("the twisted labyrinth of their mind, there was still a chance for redemption—a chance to emerge")
    print("from the shadows and reclaim their place in the light.\n\n")

    print("After multiple months of aimless travel, a small town peers into sight...\n")

#Town Functions
def town(currTown):
    while True:
        print(f"\n--------Town {currTown}--------\n")
        for person, message in towns[currTown].items():
            print(f"[{person}] {message}")
            
        print("\nTo get to the next town you have to beat the next boss\n")
        break

#Store Functions
def store():
    while True:
            storeSelect = input(f"What would you like to purchase?\n\n[0] Potion - {currPotCost}G\n[1] Temper Armor - {currArmorCost}G\n[2] Temper Sword - {currSwordCost}G\n[3] Leave\n")
            if(storeSelect.isdigit()):
                storeSelect = int(storeSelect)
                if(storeSelect == 0):
                    if(stats["Gold"] >= currPotCost):
                        stats["Gold"] -= currPotCost
                        stats["Potion"] += 1
                        print("\nYou bought one potion.\n")
                    else:
                        print("\nYou do not have enough gold.\n")
                        continue
                    
                if(storeSelect == 1):
                    if(storeStats["currArmor"] <= currMonster):
                        if(stats["Gold"] >= currArmorCost):
                            stats["Gold"] -= currArmorCost
                            stats["Def"] += 10
                        else:
                            print("\nYou do not have enough gold.\n")
                            continue
                        
                    else:
                        print("The armor has been tempered as much as it can at this town.\nTry the next town.")
                        continue
                    
                if(storeSelect == 2):
                    if(storeStats["currSword"] <= currMonster):
                        if(stats["Gold"] >= currSwordCost):
                            stats["Gold"] -= currSwordCost
                            stats["ATK"] += 10
                        else:
                            print("\nYou do not have enough gold.\n")
                            continue
                    else:
                        print("The sword has been temepered as much as it can at this town.\nTry the next town.")
                        continue
                    
                if(storeSelect == 3):
                    break
                else:
                    print("\nYour input was invalid.\n")
            else:
                print("\nYour input was invalid.\n")


#Attack Functions
def usePotion():
    if (stats["currHP"] < stats["HP"]):
        if (stats["Potion"] >= 1):
            print("You revitalize yourself with a potion.")
            stats["Potion"] -= 1
            stats["currHP"] = stats["HP"]
            if(stats["currHP"] > stats["HP"]):
                stats["currHP"] = stats["HP"]
        else:
            print("You do not have any potions.")
    else:
        print("You are already max HP")

def miniAttack():
    print("\nYou lunge at the small monster.")
    if(monStats["Def"] < stats["ATK"]):
        print("The small monster takes", stats["ATK"] - monStats["Def"],"points of damage.")
        monStats["HP"] -= (stats["ATK"] - monStats["Def"])
        print("The small monster has", monStats["HP"],"Health remaining.\n")
    else:
        print("The small monster was too strong, and took no damage!")
    
def Attack():
    print("\nYou lunge at the monster.")
    if(monStats["Def"] < stats["ATK"]):
        print("The monster takes", stats["ATK"] - monStats["Def"],"points of damage.")
        monStats["HP"] -= (stats["ATK"] - monStats["Def"])
        print("The monster has", monStats["HP"],"Health remaining.\n")
    else:
        print("The monster was too strong, and took no damage!")
    meters["sDisagree"] += 1

def TellOff():
    print("\nYou said some mean things to the monster.")
    if(monStats["Def"] < stats["ATK"]):
        print("The monster takes", stats["ATK"] - monStats["Def"],"points of emotional damage.")
        monStats["HP"] -= (stats["ATK"] - monStats["Def"])
        print("The monster has", monStats["HP"],"Health remaining.\n")
    else:
        print("The monster was too strong, and took no damage!")
    meters["disagree"] += 1

def Discuss():
    print("\nYou and the monster made small talk.")
    if(monStats["Def"] < stats["ATK"]):
        print("The monster takes", stats["ATK"] - monStats["Def"],"points of boredom damage.")
        monStats["HP"] -= (stats["ATK"] - monStats["Def"])
        print("The monster has", monStats["HP"],"Health remaining.\n")
    else:
        print("The monster was too strong, and took no damage!")
    meters["neutral"] += 1

def Play():
    print("\nYou decided to have fun with the monster.")
    if(monStats["Def"] < stats["ATK"]):
        print("The monster tires itself out, and takes", stats["ATK"] - monStats["Def"],"points of damage.")
        monStats["HP"] -= (stats["ATK"] - monStats["Def"])
        print("The monster has", monStats["HP"],"Health remaining.\n")
    else:
        print("The monster was too strong, and took no damage!")
    meters["agree"] += 1

def Befriend():
    print("\nYou tell the monster that you want to be it's good friend.")
    if(monStats["Def"] < stats["ATK"]):
        print("The monster joyfully takes", stats["ATK"] - monStats["Def"],"points of emotional damage.")
        monStats["HP"] -= (stats["ATK"] - monStats["Def"])
        print("The monster has", monStats["HP"],"Health remaining.\n")
    else:
        print("The monster was too strong, and took no damage!")
    meters["sAgree"] += 1

def EnemyAttack():
    print("The monster claws into you")
    if(stats["Def"] < monStats["ATK"]):
        print("You take", monStats["ATK"] - stats["Def"],"damage.")
        stats["currHP"] -= monStats["ATK"] - stats["Def"]
        print("You have",stats["currHP"],"HP remaining.")
    else:
        print("The monster was too weak, and did no damage!")
        
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
        
        select = input("\n[0] Attack\n[1] Tell Off\n[2] Discuss\n[3] Play\n[4] Befriend\n[5] Potion\n")
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
            elif(select == 5):
                usePotion()
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
            goldGain = currMonster * 100
            print("You gained",xpGain,"EXP points!\n")
            print("You gained",goldGain,"G!\n")
            stats["EXP"] += xpGain
            stats["Gold"] += goldGain
            lvlCheck()
            meterReset()
            currMonster += 1
            break

        EnemyAttack()

        if(stats["currHP"] <= 0):
            print("Game Over")
            input()
            exit()

def miniBattleScreen():
    while True:
        
        select = input("\n[0] Attack\n[1] Potion\n[2] Run\n\n")
        if (select.isdigit()): #Tests if select is a digit input before confirming
            select = int(select)
            if(select == 0):
                miniAttack()
                
            elif(select == 2):
                print("\nYou ran away.\n")
                break

            elif(select == 1):
                usePotion()
            
            else:
                print("\nInvalid Input, try again.")
            
        else:
            print("\nInvalid Input, try again.")
            
        if(monStats["HP"] <= 0):
            print("You slayed the small monster!")
            xpGain = (currMonster * 2)
            print("You gained",xpGain,"EXP points!")
            stats["EXP"] += xpGain
            stats["Gold"] += currMonster
            print("You gained",currMonster,"G!")
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

        if(stats["currHP"] <= 0):
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
