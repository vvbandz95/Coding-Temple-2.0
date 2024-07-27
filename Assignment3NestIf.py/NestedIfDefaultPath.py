# 1.3 Incorporate a pass statement

place = input("Choose a place: forest or cave? ")
action = input("climb a tree or cross a river?")

if place == "forest":
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
if place == "cave":
    if action == "climb a tree":
        print("Light a torch")
    elif action == "cross a river":
        print("Proceed in the dark")
    pass 
else: 
    print("You Win")