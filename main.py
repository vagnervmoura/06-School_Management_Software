# School Management Software

v_option = None
list_of_students = []
list_of_teachers = []

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


        
#print(list_of_students)
#print()
#print()

#for student in list_of_students:
#    student.describe()

def f_create():
    print("=" * 50)
    print("You are creating a new user")
    try:
        v_create = int(input("Choose your options to create:\n1 - Student\n2 - Teacher\n3 - Homeroom Teacher\n0 - To return to the main Menu\n\n"))
        if v_create == 1:
            print("You choose the option {} to create a new tudent.".format(v_create))
            while True:
                selection = input("Enter 'a' to add a new student or 'q' to quit: ")
                if selection == "q":
                    break
                elif selection == "a":
                    name = input("Enter the name of the student: ")
                    classe = input("Enter the class of the student: ")
        
                    new_student = Student(name=name, classe=classe)
                    list_of_students.append(new_student)
                    print(f"student {name} added")
        
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
                    list_of_teachers.append(new_teacher)
                    print(f"teacher {name} added")
        
    except ValueError:
        print("Sorry, you did not input a valid value.\n")          
    
    
def f_manage():
    print("You are managing the sytem")
    
    
# MAIN MENU
line = 1
while v_option != 0:
    v_option = int(input("\n\nSelect one of the following options:\n1 - Create\n2 - Manage\n0 - end\n\n"))

    try:
        if v_option == 0:
            print("\nThank you for using our system.\n\n")
            exit()
            
        elif v_option == 1: # option to CREATE
            print("You choose the v_option {} to Create.".format(v_option))
            f_create()
            
        elif v_option == 2: # option to MANAGE
            print("You choose the v_option {} to Manage.".format(v_option))
            f_manage()
    
    except ValueError:
        print("Sorry, you did not input a valid value.\n")  
        
        
        
# CREATE Process


# MANAGE Process

