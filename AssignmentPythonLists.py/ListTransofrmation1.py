# You've been given a list of grades from an exam. You need to process and analyze these grades.
# Task 1: Given the list of grades:
# grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
# Sort the grades in descending order and print the sorted list.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort()
print(grades)

# Task 2: Calculate the average grade and print it.
total_grades = sum(grades)
num_grades = len(grades)

ave_grade = total_grades / num_grades
print("Average grade:", ave_grade)