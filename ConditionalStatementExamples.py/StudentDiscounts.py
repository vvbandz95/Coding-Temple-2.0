#3 2.4 EXAMPLE 3 

grade = input("Enter your grade (A/B/C): ")
sports_team = input("Are you part of the sports team? (yes/no): ")
drama_club = input("Are you part of the drama club? (yes/no): ")

discount = 0 

if grade == 'A':
    if sports_team == 'yes':
        discount = 20 
    else:
        discount = 10 
elif grade == 'B':
    if drama_club == 'yes':
        discount = 15


print(f"You are eligible for a {discount}%  discount.")