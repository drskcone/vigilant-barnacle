grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Emma": 88
}
totalscore = 0
for score in grades.values():
    totalscore += score
average = totalscore/5
print("The class Average is:", average)

highest_student = max(grades, key=grades.get)
lowest_student = min(grades, key=grades.get)
print("\nTop Scorer:")
print(highest_student, "=", grades[highest_student])
print("Bottom Scorer:")
print(lowest_student, "=", grades[lowest_student])

search_name = input("\nEnter students name that you want to look up: ")
grade = grades.get(search_name)
if grade is not None:
    print(search_name, "'s grade is", grade)
else:
    print("Student not found in the grade book, make sure youre using Capitals.")
