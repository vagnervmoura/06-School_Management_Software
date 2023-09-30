all_usernames = []

def print_hello_world(separator, first_thing_to_print, age=None):
    print(separator * 23)
    print("This is the first print")
    if age is not None:
        print("You are {} years old".format(age))
    username = input("Enter your name: ")
    all_usernames.append(username)
    if username == "Vagner":
        return "Welcome {}".format(username)
    else:
        return "{}, You are not Vagner".format(username)
    
    
return_value = print_hello_world(separator="*", first_thing_to_print="This is the first run", age=21)
print("Returned Value:", return_value)

return_value = print_hello_world(first_thing_to_print="This is the seccond run", separator="=", age=42)
print("Returned Value:", return_value)

return_value = print_hello_world("*", "This is the first run")
print("Returned Value:", return_value)


print("All usernames:", all_usernames)