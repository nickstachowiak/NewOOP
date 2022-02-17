from datetime import datetime

import StudentClass as sc

def main():
    studentid = input('What is your student ID?: ')
    dob = int(input('What year were you born?: '))
    name = input('What is your name?: ')
    classification = input('What is your classification?: ')

    student = sc.Student(studentid,name,dob,classification)
    student.age()
    print('The students age is: ', student.get_age())
    student.registration()

main()

