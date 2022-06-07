import random
import pandas

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word:len(word) for word in sentence.split()}
print(result)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

student_grades = {name: random.randint(1, 100) for name in names}
print(f"student grades: {student_grades}")

passed_students = {
    student: grade
    for (student, grade) in student_grades.items() if grade >= 60
}
print(f"passed students: {passed_students}")

grades = [random.randint(1, 100) for _ in range(6)]

student_dict = {
    "student": names,
    "score": grades
}
print(student_dict)

student_data_frame = pandas.DataFrame(student_dict)

print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(f"student: {row.student}\tscore: {row.score}")
