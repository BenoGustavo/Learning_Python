from os import system,_exit
import json

to_do = []
undo = []
remake = []

FILE_PATH = 'Python-Projects/python-udemy/Sessão_2_Modulos_E_Funções/files/to_do_list.json'

#reading archive
try:
    with open(FILE_PATH, 'r', encoding='utf8') as archivejson: 
        to_do = json.load(archivejson)

#If not found create
except FileNotFoundError:
    with open(FILE_PATH, 'w', encoding='utf8') as arquivo_txt:
        pass

def saving_on_json(path,list):
    with open(path, 'w', encoding='utf8') as archivejson: 
        json.dump(list, archivejson, indent=2)

# infinite loop
while True:
    right_value_flag = False

    system("cls")

    # Menu text
    print("What do you want to do?\n[Add] - to add something to the list\n[Read] - Read all itens from the list\n[Undo] - to bring the list back one action\n[Remake] - to undo the last undo\n[Exit] - Take a break from coding")
    user_choice = input().lower()

    
    if user_choice == "add":
        system("cls")

        add_to_list = input("Insert what do you want to add to the list: ")
        try:
            while right_value_flag is False:

                hour_add_to_list = int(input("Insert what hours you will do that: "))
                minute_add_to_list = int(input("Insert what minute you will do that: "))

                if minute_add_to_list > 60:
                    while minute_add_to_list > 60:
                        minute_add_to_list += -60
                        hour_add_to_list += 1

                if hour_add_to_list > 24:
                    raise ValueError

                right_value_flag = True

        except ValueError:
            system("cls")
            input("Write a valid value between 0 - 9...\n\nPress any keys to continue")
            input("\nPress any key to continue...")

        ready_to_add = add_to_list + " - " + str(hour_add_to_list) + ":" + str(minute_add_to_list)

        to_do.append(ready_to_add)

        saving_on_json(FILE_PATH,to_do)

        input(ready_to_add + " - added successfully, press any button to continue...")

        continue

    if user_choice == "read":
        #if there is no item in the list
        if len(to_do) == 0:
            
            input("\nFirst add a value to the list, press any key to return")
            continue

        print("\nThese are the itens there are in the list\n")
        for item in to_do:
            print(item)
        
        input("\nPress any key to return...")
        continue

    if user_choice == "undo":
        system("cls")

        #if there is no item in the list
        if len(to_do) == 0:
            
            input("\nFirst add a value to the list, press any key to return")
            continue
        
        print("\nThese are the itens there are in the list\n")
        for index,item in enumerate(to_do):
            print(str(index) + " | " + item + "\n")

        user_choice = input("Insert the index that you want to delete or [return]: ")

        if user_choice.isnumeric():
            undo.append(to_do.pop(int(user_choice)))

            input(undo[len(undo) - 1] + " - deleted successfully, press any button to continue...")

            saving_on_json(FILE_PATH,to_do)

        elif user_choice.lower() == 'return':
            continue

        else:
            input("Invalid value, press any button to return...")
        continue

    if user_choice == "remake":
        system("cls")

        if len(undo) == 0:
            input("First add a value to the list, press any key to return")
            continue

        to_do.append(undo.pop())

        saving_on_json(FILE_PATH,to_do)

        continue

    if user_choice == "exit":
        system("cls")
        
        user_choice = input("Do you realy want to exit, you will lose all your cached info. [Y] or [N]")

        saving_on_json(FILE_PATH,to_do)

        if user_choice.lower() == 'y':
            _exit(1)
        else:
            continue
        
    else:
        input("\nPlease enter a valid value, press any button to continue...")
        continue
