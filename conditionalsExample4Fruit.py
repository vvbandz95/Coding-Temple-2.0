#4 Fruit

fruit = "Apple"
is_ripe = True
has_spots = False 

if fruit == "Apple":
    if is_ripe and not has_spots:
        print("Perfect for a juicy bite!")
    elif not is_ripe and not has_spots:
        print("Let it ripen")
    else: 
        print("Might be best for apple pie!")
elif fruit == "Banana":
    if is_ripe and not has_spots:
        print("Ready to eat!")
    elif not is_ripe:
        print("Still a bit green.")
    else:
        print("Perfect for banana bread!")
else:
    print("Not sure")