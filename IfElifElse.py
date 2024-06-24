moon_phase = "full moon" 

if moon_phase == "full moon":
    print("Witches' night out!")

# 2 
moon_phase = "full moon" 
if moon_phase == "full moon":
    print("beware of werewolves")


#3
elif moon_phase == "new moon":
    print("Witches night") 

#4 checks if potion is greater than 10 or greater than 10 and less than 20 
potion_strength = 15 

if potion_strength > 20:
    print("It's a super potent potion")
    
elif potion_strength > 10:
    print("it's a moderately  potent potion")

#5 if, elif 
weather = "rainy"

if weather == "sunny": 
    print("It's a bright and beautiful day!")

if weather == "rainy": 
    print("Carry an umbrella!")

elif weather == "snowy":
    print("Time to build a snowman!")

#6
sword_material = "silver"

if sword_material == "gold":
    print("The sword shines brightly!")
elif sword_material == "silver": 
    print("The sword has a mystical glimmer!")
elif sword_material == "bronze":
    print("its valuable!")

#7 
player_level = 12
if player_level < 5:
    print("access beginner")
elif 5<= player_level < 10: 
    print("Enter the intermediate dungeon!")
elif player_level >= 10:
    print("Challenge the advanced dungeon")

#8
is_dragon_present = True
has_treasure = False 

if is_dragon_present and not has_treasure: 
    print("Enter with caution!")
elif not is_dragon_present and has_treasure: 
    print("Grab the treasure!")
elif is_dragon_present and has_treasure:
    print("A mighty dragon guards the treasure!")
else:
    print("Empty lair. Safe to explore, but no treasures here.")

# 9 ELSE STATEMENTS 9.1 Waether wardrobe guide 
is_raining = False 
is_cold = True 

if is_raining and is_cold:
    print("Wear a waterproof jacket and a scarf!")
elif is_raining: 
    print("Don't forget your umbrella!")
else:
    print("Looks like a clear day, dress as you wish!")

# 9.2 Monthly Savings Calculator
income = 5000
expenses = 4500

savings = income - expenses

if savings > 1000: 
    print("Great job! You saved a lot this month.")
elif savings <=0:
    print("Looks lke you've spent all or more than you earned!")
else: 
    print("Every little bit counts! Keep saving.")