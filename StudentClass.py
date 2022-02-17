from datetime import date


class Student:

    def __init__(self, studentid, name, dob, classification):
        self.__StudentID = studentid
        self.__name = name
        self.__dob = dob
        self.__classification = classification

    def age(self):
        today = date.today()
        self.__age = today.year - int(self.__dob)

    def get_age(self):
        return self.__age

    def registration(self):
        if self.__classification == 'F':
            print('Registration Open: 11/10 - 11/12')
        elif self.__classification == 'S':
            print('Registration Open: 11/7 - 11/9')
        elif self.__classification == 'J':
            print('Regristration Open: 11/4 - 11/6')
        else:
            print('Registration Open: 11/1 - 11/3')


