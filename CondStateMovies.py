#3 Movies are windows to diverse worlds, offering entertainment, education, inspo. not all films are suitable for every age group given their content, themes, visuals. Movies come with specific ratings. Given a rating (G, PG, PG-13, R) and the age person, infor the user if they can watch the movie based on ther age 

age = int(input("Enter your age: "))
rating = input("Enter movie rating (G, PG, PG-13, R): ")

if rating == "G":
    print(" You can watch the movie!")
elif rating == "PG" and age >= 7:
    print("You can watch the movie!")
elif rating == "PG-13" and age >= 13: 
    print("You can watch the movie!")
elif rating == "R" and age >= 17: 
    print("You can watch the movie!")
else: 
    print("You are not allowed to watch this movie")
