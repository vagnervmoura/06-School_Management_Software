# School Management Software

v_option = None


def goto(linenum):
    global line
    line = linenum

def f_create():
    print("You are creating a new user")
    
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

