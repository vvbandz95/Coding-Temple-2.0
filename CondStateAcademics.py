#4 Academic performance is gauged through grades which serve as an understanding of a student's understanding, effort and mastery of a subject. They are typically represented numerically or as letter gradws. So, convert numeric grades to letter grades. Assume grades are between 0 to 100. 

grade = float(input("Enter your grade (0-100): "))

if grade >= 90:
    print("Your letter grade is A.")
elif grade >= 80:
    print("Your letter grade is B.")
elif grade >= 70:
    print("Your letter grade is C.")
elif grade >= 60:
    print("Your letter grade is D.")
else:
    print("Your letter grade is F.")