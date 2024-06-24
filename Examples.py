# Conditional Statements Examaples, using if, comparison operator and 
# if, is not !=
enemy = "goblin"

if enemy != "dragon":
    print("Charge forward, brave adventure!")

# if and checking conidtion using lower oprator

player_health = 75 

if player_health <= 100:
    print("Drink a health potion for full strength")

# if statements and checking if condition is in a range

magic_stone = 12 

if 10 <= magic_stone <20: 
    print("You've unlocked the Eleven Chest!")

# False, True 0m describes situation or environment, using not operator, checking 2 conditions 

is_daytime = False
dragon_asleep = True

if not is_daytime and dragon_asleep: 
    print("Sneak into the dragon's lair to retrieve the golden chalic!" )

is_daytime = True
dragon_asleep = True

if not is_daytime and dragon_asleep: 
    print("Sneak into the dragon's lair to retrieve the golden chalic!" )

is_daytime = True
dragon_asleep = False

if not is_daytime and dragon_asleep: 
    print("Sneak into the dragon's lair to retrieve the golden chalic!" )

# if statement 

torch_lit = True

if torch_lit:
    print("Venture forth into the cave!")

torch_lit = False

if torch_lit:
    print("Venture forth into the cave!")

# store information about current conditions, and wehter its true or not

weather = "sunny" 

if weather == "sunny":
    print("Time for a picnic!")

# if statement checking 2 conidtions using and operator 

gold_coins = 10
silver_coins = 50 

if gold_coins > 5 and silver_coins > 30: 
    print("Enought to buy the magic potion!")

# if statement using not equal to ( != )

enemy = "goblin"

if enemy != "dragon":
    print("Charge forward,brave adventure")