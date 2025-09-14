student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for key, value in student_grades:
    if 91 <= value <= 100:
        student_grades[key] = "outstanding"
    elif 81 <= value <= 90:
        student_grades[key] = "exceeds expectations"
    elif 71 <= value <= 80:
        student_grades[key] = "acceptable"
    elif value <= 70:
        student_grades[key] = "fail"

print(student_grades)

