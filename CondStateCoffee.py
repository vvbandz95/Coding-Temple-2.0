#6 Coffee is diverse and many people drink it. There are a variety of perfect brews for everyone. But with lots of options, how does 1 decide? Recommend a type of coffee based on user preference about sweetness and milk 

likes_sweet = input("Do you like your coffee sweet? (yes/no)")
likes_milk = input("Do you like milk in your coffee? (yes/no)")

if likes_sweet == 'yes' and likes_milk == 'yes':
    print("How about a caramel latte")
elif likes_sweet == 'no' and likes_milk == 'yes':
    print("An americano with a dash of milk sounds good")
elif likes_sweet == 'yes' and likes_milk == 'no': 
    print("Tray a black coffess, 2 sugar cubes")
else: 
    print("Black coffess it is")