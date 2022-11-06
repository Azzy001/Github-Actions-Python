person_list = []

def person():
    global person_list
    first = input("Enter firstname: ")
    last = input("Enter lastname: ")
    age = int(input("Enter age: "))
    person_object = first, last, age
    person_list.append(person_object)
    print(person_list)
    

while True:
    try:
        choice = input("Would you like to add a person? [Y|N]: ")
        if (choice == "Y") or (choice == "y"):
            person()
            
        elif (choice == "N") or (choice == "n"):
            print("Goodbye!")
            break
        
        else:
            print("Goodbye--")
            break
            
    except ValueError:
        print("Please try again")
