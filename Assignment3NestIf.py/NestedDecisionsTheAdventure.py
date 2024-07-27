# 1 Nested Decisions: The Adventure Game; fix the code 

place = input("Choose a place: forest or cave? ")
action = input("climb a tree or cross a river?")

if place == "forest":
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif  place == "cave":
    print("You find a hidden treasure!")
