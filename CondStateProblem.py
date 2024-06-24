#7 Create a proram for a library to calculate fines for overdue books. Following fine structure 
# $1 per day for books that are up to 5 days overdue 
# $2 per day for books that are 6 to 10 dayhs overdue
# $5 per day for more than 10 days overdue 

# Write a python program that: 
# 1. Asks the user for the number of days a book is overdue
# 2. Calculates the fine based on the above criteria 
# 3. Displays the fine amount 

days_overdue = int(input("How many days is the book overdue?"))
fine = 0

if  days_overdue <= 5:
    fine = days_overdue * 1
elif days_overdue <= 10:
    fine = days_overdue * 2
else:
    fine = days_overdue * 5

print(f"Your fine is ${fine}.")