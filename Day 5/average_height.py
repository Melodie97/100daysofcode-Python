student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum_heights = 0
for height in student_heights:
    sum_heights += height
print(sum_heights)

num_of_students = 0
for num in num_of_students:
    num_of_students += 1
print(num_of_students)

avg_height = round(sum_heights/num_of_students)
print(avg_height))
