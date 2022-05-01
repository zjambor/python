"""
Write a program that asks the user for given name, surname and field of study for a student. Store this data in a tuple and print the tuple. 
Below is an example execution of the program.

Please enter the given name of the student: Harry 
Please enter the surname of the student: Potter 
Please enter the filed of study of the student: Defence Against the Dark Arts 
('Harry', 'Potter', 'Defence  Against the Dark Arts')
"""

given_name = input("Please enter the given name of the student: ")
surname = input("Please enter the surname of the student: ")
study = input("Please enter the filed of study of the student: ")

my_tuple = (given_name, surname, study)
print(my_tuple)