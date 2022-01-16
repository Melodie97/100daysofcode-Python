student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}


student_grades = {}
for name in student_scores:
    if student_scores[name] >= 91:
        student_grades[name] = "Outstanding"
    elif student_scores[name] >= 81 and student_scores[name] <= 90:
        student_grades[name] = "Exceeds Expectations"
    elif student_scores[name] >= 71 and student_scores[name] <= 80:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"


print(student_grades)
