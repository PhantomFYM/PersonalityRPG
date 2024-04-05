#Attack Functions
def Attack:
    print("You lunge at the enemy")
    enemyHP -= (ATK - enemyDef)
    sDisagree += 1

def TellOff:
    enemyHP -= (ATK - enemyDef)
    disagree += 1

def Discuss:
    enemyHP -= (ATK - enemyDef)
    neutral += 1

def Play:
    enemyHP -= (ATK - enemyDef)
    agree += 1

def Befriend:
    enemyHP -= (ATK - enemyDef)
    sAgree += 1
    
def Enemy1:
    enemyHP = 5
    enemyATK = 2
    enemyDef = 3

#Default Stats
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

select = 0

while True:
    print("[0] Attack\n[1] Tell Off\n[2] Discuss\n[3] Play\n[4] Befriend")
    int(input())
    if(select == 0):
    elif(select == 1):
    elif(select == 2):
    elif(select == 3):
    elif(select == 4):

