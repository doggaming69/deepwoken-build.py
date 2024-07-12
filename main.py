import random #DEEPWOKEN BUILD RANDOMIZER 

def weapon():
    Weapon = ["light", "medium", "heavy","legendary"]
    weapon_choose = random.choice(Weapon)
    return weapon_choose

def attunement():
    Attunement = ["flamecharm", "shadowcast", "frostdraw", "ironsing", "thundercall", "galebreath", "attunementless"]
    attunement_choose = random.choice(Attunement)
    return attunement_choose

def oath():
    Oath = ["oathless", "jetstriker", "blindseer", "dawnwalker", "fadetrimmer", "contractor", "linkstrider", "visionshaper", "starkindred",'saltchemist','arcwarder']
    Oath_choose = random.choice(Oath)
    return Oath_choose

def archetype():
    Archetype = ['tank', 'damage dealer', 'support', 'mage', 'anti healer']
    Archetype_choose = random.choice(Archetype)
    return Archetype_choose

def bell_usage():
    Bell_usage = ["gank bell", "support bell", "1v1 bell", "misc (teleport kamui etc)"]
    Bell_usage_choose = random.choice(Bell_usage)
    return Bell_usage_choose

def medium_weapon():
    Medium_weapon = ['sword','spear','rifle','Hero blade','purple cloud']
    Medium_weapon_choose = random.choice(Medium_weapon)
    return Medium_weapon_choose

def light_weapon():
    Light_weapon = ['dagger','fist','rapier','guns','jus karita','cerulean thread']
    Light_weapon_choose = random.choice(Light_weapon)
    return Light_weapon_choose

def heavy_weapon():
    Heavy_weapon = ['greataxe','halberd','greathammer','misc','pale briar']
    Heavy_weapon_choose = random.choice(Heavy_weapon)
    return Heavy_weapon_choose

def legendary_weapon():
    Legendary_weapon = ['old (curved crypt etc.)','new (deepspindle kyrswynter etc.)','wyrmtooth',]
    Legendary_weapon_choose = random.choice(Legendary_weapon)
    return Legendary_weapon_choose

while True:
    deepwoken = input("Press any key to continue, or Enter to exit: ")
    if deepwoken != "":
        break

print("Weapon:", weapon())
print("Attunement:", attunement())
print("Oath:", oath())
print("Archetype:", archetype())
print("Bell Usage:", bell_usage())
while True:
    deepwoken2 = input ('enter weapon type that you recieved (type no if you want the freedom to choose it urself)')
    if deepwoken2 !="":
        break
if deepwoken2 == ('medium'):
    print ("Weapon variant:", medium_weapon())
if deepwoken2 == ('heavy'):
    print ("Weapon variant:", heavy_weapon())
if deepwoken2 == ('light'):
    print ("Weapon variant:",light_weapon())
if deepwoken2 == ('legendary'):
    print ("Weapon variant",legendary_weapon())
