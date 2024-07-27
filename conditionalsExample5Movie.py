#5 Movies

movie = "Inception"
release_year = 2010 #integer to represent the year
duration_min = 148 # Using an integer for movie's duration 

if movie == "Incpetion": 
    if 2000 <= release_year <= 2020 and duration_min > 120:
        print("A modern calssic with runtime over 2 hours!")
    elif release_year < 2000:
        print("A gem from the past!")
    else: 
        print("A recent masterpiece!")
elif movie == "Titanic":
    if release_year == 1997 and duration_min > 180:
        print("a romantic epid that spans over 3 hours!")
    else:
        print("A timeless love story!")
else:
    print("Enjoy the movie!")