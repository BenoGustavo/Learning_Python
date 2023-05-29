from os import system

to_do = []
undo = []
remake = []

#infinite loop
while True:
    right_value_flag = False
    system("cls")

    #Menu text
    print("What do you want to do?\n[Add] - to add something to the list\n[Del] - to delete something from the list\n[Undo] - to bring the list back one action\n[Remake] - to undo the last undo\n[Exit] - Take a break from coding")
    user_choice = input().lower()

    while right_value_flag is False:
        if user_choice == "add":
            add_to_list = input("Insert what do you want to add to the list: ")
            try:
                time_add_to_list = int(input("And what time do you will do that: "))
                
                right_value_flag = True
            except:
                system("cls")
                input("Write a valid value between 0 - 9...\n\nPress any keys to continue")

            ready_to_add = add_to_list + " - " + time_add_to_list

        continue
    if user_choice == "del":
        input("del")

        continue
    if user_choice == "undo":
        input("undo")

        continue
    if user_choice == "remake":
        input("remake")

        continue
    if user_choice == "exit":
        input("exit")

        continue
    else:
        input("Please enter a valid value, press any button to continue...")
        continue
