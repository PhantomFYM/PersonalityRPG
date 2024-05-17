from Functions import *

#Player Stats
stats = {
"Gold": 0,
"Potion": 0,
"EXP": 0,
"LVL": 1,
"HP": 10,
"currHP": 10,
"Def": 0,
"ATK": 5,
}

#Enemy Stats
monStats = {
"HP": 0,
"Def": 0,
"ATK": 0,
}

#Enemy Check
currMonster = 1

#BattleResults
eResults = {}

#Store Stats
storeStats = {
"currArmor": 1,
"currSword": 1,
}

currArmorCost = storeStats["currArmor"] * 10
currSwordCost = storeStats["currSword"] * 10
currPotCost = currMonster * 25

#Rest Stats
currRestCost = currMonster * 5

#Boss monster stats
monStatMap = {
1: (45, 50, 2), #Enemy1
2: (90, 40, 10), #Enemy2
3: (150, 100, 30), #Enemy3
4: (200, 400, 50), #Enemy4
5: (300, 1000, 100), #Enemy5
}

miniMonStatMap = {
1: (10, 2, 0),
2: (30, 25, 2),
3: (60, 40, 5),
4: (130, 100, 10),
5: (160, 250, 30),
}

#Agreement Meters
meters = {
"sDisagree": 0,
"disagree": 0,
"neutral": 0,
"agree": 0,
"sAgree": 0,
}



#Town texts
towns = {
1: {
"Bob": "Hello Traveler! Here is info.",
"Louis": "Hello, be careful there are monsters around.",
"Sarah": "What's up."
},
2: {
"John": "Good job! You made it to the next town.",
"Percy": "Wow, that's impressive.",
"Jewel": "Interesting..."
},
3: {
"Mark": "Oh, you think you accomplished something?",
"Cleo": "How strange",
"Sam": "You have a long way to go."
},
4: {
"Dean": "Wow..!",
"Emily": "If you want to know more keep going.",
"Susan": "So how where the monsters?"
},
5: {
"Lily": "Well well...",
"Joseph": "Wow I can't believe you made it this far.",
"Steve": "Good job for making it this far!"
},
}

#Story Calls


#Main Menu
while True:
    menuSelect = input("\n--------Personality RPG--------\n\n[0] Start\n[1] Credit\n")
    if(menuSelect.isdigit()):
        menuSelect = int(menuSelect)

        if(menuSelect == 0):

            intro()

            #Area Menu
            while True:
                if(currMonster < 6):
                        
                    townSelect = input("\n[0] Town\n[1] Area\n[2] Shop\n[3] Advance\n[4] Stats\n[5] Rest\n")
                    if(townSelect.isdigit()):
                        townSelect = int(townSelect)

                        if(townSelect == 0):
                            town(currMonster)
                            continue

                        if(townSelect == 1):
                            print("\nYou encounter a small monster in the surrounding area!\n")
                            setMonStats(*miniMonStatMap.get(currMonster, (0, 0, 0)))
                            miniBattleScreen()
                            continue

                        if(townSelect == 2):
                            store()
                            continue
                            
                        if(townSelect == 3):
                            setMonStats(*monStatMap.get(currMonster, (0, 0, 0))) #Unpacks and repacks tuple, as well as record enemy stats.
                            BattleScreen()
                            continue

                        if(townSelect == 4):
                            print(f"\nGold - {stats['Gold']}\nPotions - {stats['Potion']}\n\nExperience - {stats['EXP']}\nLevel - {stats['LVL']}\n\nMax HP - {stats['HP']}\nHP - {stats['currHP']} \n\nATK - {stats['ATK']}\nDEF - {stats['Def']}\n")
                            continue
                        
                        if(townSelect == 5):
                            #Rest selection
                            print(f"Would you like to rest in town for {currRestCost}G?")
                            sleepSelect = input("\n[0] Yes\n[1] No\n")
                            if(sleepSelect.isdigit()):
                                sleepSelect = int(sleepSelect)
                                
                                if(sleepSelect == 0):
                                    if(stats["Gold"] >= currRestCost):
                                        stats["Gold"] -= currRestCost
                                        print("\nYou rest in town, cozy in these dreadful lands...\n\nHP fully restored!\n")
                                        stats["currHP"] = stats["HP"]

                                    else:
                                        print("You do not have enough Gold\n")

                                if(sleepSelect == 1):
                                    continue
                            else:
                                print("\nInvalid Input, try again.\n")
                                
                        else:
                            print("\nInvalid Input, try again.\n")
                        
                    else:
                        print("\nInvalid Input, try again.\n")

                else:
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

        #Credit
        if(menuSelect == 1):
            print("\nKyleigh Marlowe - Town Talks\n\nJudah McBee - General Systems & Intro\n\nDaniela Olvera - Personality Systems\n")
            
        else:
            print("\nInvalid Input, try again.")
    else:
        print("\nInvalid Input, try again.")
