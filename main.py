# School Management Software

# on terminal to execute this EMPLOYEE CLASSES and get the inputs from a text file "employees.txt"
# type on terminal: Get-Content input_school.txt | python main_test_school.py 

import re

v_option = None
list_of_students = []
list_of_teachers = []
list_of_homeroom_teachers = []
v_name = None
v_classe = None
number = 0
classe_of_students = []


def goto(linenum):
    global line
    line = linenum
    
    
class Student:
    def __init__(self, name, classe):
        self.name = name
        self.classe = classe
        
    def describe(self):
        print(f"{self.name} studies in {self.classe}")
        

class Teacher:
    def __init__(self, name, subject, classe):
        self.name = name
        self.subject = subject
        self.classe = classe

class HomeroomTeacher(Teacher):
    def __init__(self, name, classe, students):
        super().__init__(name, classe, students)
        self.students = students
        
    def describe(self):
        print(f"{self.name} teaches in {self.classe} and has {self.students} students")


def f_create():
    print("=" * 50)
    print("You are creating a new user")
    try:
        v_create = int(input("Choose your options to create:\n1 - Student\n2 - Teacher\n3 - Homeroom Teacher\n0 - To return to the main Menu\n\n"))
        if v_create == 1:
            print("You choose the option {} to create a new student.".format(v_create))
            while True:
                selection = input("Enter 'a' to add a new student or 'q' to quit: ")
                if selection == "q":
                    break
                elif selection == "a":
                    name = input("Enter the name of the student: ")
                    classe = input("Enter the class of the student: ")
        
                    new_student = Student(name=name, classe=classe)
                    student_name = new_student.name
                    student_classe = new_student.classe
                    list_of_students.append({"v_name": student_name, "v_classe": student_classe})
                    print(f"student {name} added")
                else:
                    print(f"{selection} is not an valid option.\n")
        
        elif v_create == 2:
            print("You choose the option {} to create a new teacher.".format(v_create))
            while True:
                selection = input("Enter 'a' to add a new teacher or press 'ENTER'to quit to main menu: ")
                if selection == "":
                    break
                elif selection == "a":
                    name = input("Enter the name of the teacher: ")
                    subject = input("Enter the subject of the teacher: ")
                    classe = input("Enter the class of the teacher: ")
        
                    new_teacher = Teacher(name=name, subject=subject, classe=classe)
                    teacher_name = new_teacher.name
                    teacher_subject = new_teacher.subject
                    teacher_classe = new_teacher.classe
                    list_of_teachers.append({"v_name": teacher_name, "v_subject": teacher_subject, "v_classe": teacher_classe})
                    print(f"teacher {name} added")
                else:
                    print(f"{selection} is not an valid option.\n")
                    
        elif v_create == 3:
            print("You choose the option {} to create a new Homeroom Teacher.".format(v_create))
            while True:
                selection = input("Enter 'a' to add a new Homeroom Teacher or press 'q'to quit to main menu: \n")
                print(f"You choose the option {selection}\n")
                if selection == "q":
                    break
                elif selection == "a":
                    name = input("Enter the name of the Homeroom Teacher: ")
                    classe = input("Enter the class of the Homeroom Teacher: ")
                    for students_in_classe in list_of_students:
                        if students_in_classe["v_classe"] == classe:
                            classe_of_students.append(students_in_classe["v_name"])
                    print()                                              
                    new_homeroom_teacher = HomeroomTeacher(name=name, classe=classe, students=classe_of_students)
                    homeroomTeacher_name = new_homeroom_teacher.name
                    homeroomTeacher_classe = new_homeroom_teacher.classe
                    homeroomTeacher_students = new_homeroom_teacher.students
                    list_of_homeroom_teachers.append({"v_name": homeroomTeacher_name, "v_classe": classe, "v_students": homeroomTeacher_students})
                    
                    number_of_students = len(list_of_homeroom_teachers) + 1
                    print(f"Homeroom Teacher {name} added")
                    print()
                    print()                    
                else:
                    print(f"{selection} is not an valid option.\n")                    
        elif v_create == 0:
            print("You choose the option {} to return to the main Menu.".format(v_create))
            print()
            print()            
        else:
            print(f"{v_create} is not an valid value.\n")        
    except ValueError:
        print("Sorry, you did not input a valid value.\n")          
    
    
def f_manage():
    print("=" * 50)
    print("You are managing the sytem")
    
    try:
        v_manage = int(input("Choose your options to manage:\n1 - Class\n2 - Student\n3 - Teacher\n4 - Homeroom Teacher\n0 - To return to the main Menu\n\n"))        
        if v_manage == 1: #  - 'class': Prompt for a class to display (e.g., "3C"), the program should list all students in the class and the homeroom teacher.
            print("You choose the option {} to manage a class.".format(v_manage))
            classe = input("Enter the class you want to manage, or press 'q' to quit: \n")
            print(f"Class Selected: {classe}")
            while classe != "q":
                for manage_classe in list_of_homeroom_teachers:
                    if manage_classe["v_classe"] == classe:
                        print(f"Homeroom teacher for class {classe}: {manage_classe['v_name']}")
                        print(f"List of students in class: ")
                        print(*manage_classe["v_students"], sep = "\n")                   
                else:
                    break  
                
        elif v_manage == 2: # - 'student': Prompt for a student's first and last name, the program should list all the classes the student attends and the teachers of these classes.
            print("You choose the option {} to manage a student.".format(v_manage))
            student_name = input("Enter the name of the student you want to manage, or press 'q' to quit: \n")
            print(f"Student Selected: {student_name}\n\n")
            print(f"The student {student_name} is in the following classes: ")
            while student_name != "q":
                for manage_student in list_of_students:
                    if manage_student["v_name"] == student_name:
                        print(manage_student['v_classe'])
                        
                for manage_teacher_of_student in list_of_teachers:
                    for manage_student in list_of_students:
                        if manage_student["v_name"] == student_name:
                            if manage_teacher_of_student["v_classe"] == manage_student["v_classe"]:
                                print(f"The teacher of the class {manage_student['v_classe']} is {manage_teacher_of_student['v_name']}")               
                break                               

        elif v_manage == 3: #  - 'teacher': Prompt for a teacher's first and last name, the program should list all the classes the teacher teaches.
            print("You choose the option {} to manage a teacher.".format(v_manage))
            teacher_name = input("Enter the name of the teacher you want to manage, or press 'q' to quit: \n")
            print(f"Teacher Selected: {teacher_name}\n\n")
            print(f"The teacher {teacher_name} teaches the following classes: ")
            while teacher_name != "q":
                for manage_teacher in list_of_teachers:
                    if manage_teacher["v_name"] == teacher_name:
                        print(manage_teacher['v_classe'])
                break
            
        elif v_manage == 4: #  - 'homeroom teacher': Prompt for a homeroom teacher's first and last name, the program should list all students the homeroom teacher leads.
            print("You choose the option {} to manage a homeroom teacher.".format(v_manage))
            homeroomTeacher_name = input("Enter the name of the homeroom teacher you want to manage, or press 'q' to quit: \n")
            print(f"Homeroom Teacher Selected: {homeroomTeacher_name}\n\n")
            print(f"The homeroom teacher {homeroomTeacher_name} leads the following students: ")
            while homeroomTeacher_name != "q":
                for manage_homeroomTeacher in list_of_homeroom_teachers:
                    if manage_homeroomTeacher["v_name"] == homeroomTeacher_name:
                        print(*manage_homeroomTeacher["v_students"], sep = "\n")
                break
            
        elif v_manage == 0:
            print("You choose the option {} to return to the main Menu.".format(v_manage))
            print()
            print()

        else:
            print(f"{v_manage} is not an valid value.\n") 

    except ValueError:
        print("Sorry, you did not input a valid value.\n")  
    
# MAIN MENU
line = 1
while True:
    print()
    print(" "*6+"/" * 50 + "\n" +" "*6+ "/" + " " * 12 + "School Management System" + " " * 12 + "/" + "\n" +" "*6+ "/" * 50)
    print(" "*6+"/" + " " * 48 + "/", sep="")
    print(" "*6+"/"+" "*6+"Select one of the following options:"+" "*6+"/")
    print(" "*6+"/"+" "*6+"="*36+" "*6+"/")
    print(" "*6+"/"+" "*15+"1 - Create"+" "*23+"/")
    print(" "*6+"/"+" "*15+"2 - Manage"+" "*23+"/")
    print(" "*6+"/"+" "*15+"0 - end"+" "*26+"/")
    print(" "*6+"/" + " " * 48 + "/", sep="")
    print(" "*6+"/" * 50)

    try:
        v_option = int(input())
        
        if v_option == 0:
            print("\nThank you for using our system.\n\n")
            exit()
            
        elif v_option == 1: # option to CREATE
            print("You choose the option {} to Create.".format(v_option))
            f_create()
            
        elif v_option == 2: # option to MANAGE
            print("You choose the option {} to Manage.".format(v_option))
            f_manage()
            
        else:
            print(f"{v_option} is not an valid option.\n")
    
    except ValueError:
        print("Sorry, you did not input a valid option.\n")  