"""
Implement a function named get_student_data(). The function should do the following:

    Using input() it asks for name, first name and a student-id.
    The values are packed into a tuple.
    This tuple is returned from the function.

The function get_student_data() is then called in the program, the return value is assigned to a variable. Finally, output the variable using print().
"""

def get_student_data():
    name = input("Name: ")
    firstname = input("First name: ")
    student_id = int(input("Student id: "))
    return (name, firstname, student_id), (name, firstname, student_id+1)

student_data1, student_data2 = get_student_data()
print(student_data1, student_data2)

