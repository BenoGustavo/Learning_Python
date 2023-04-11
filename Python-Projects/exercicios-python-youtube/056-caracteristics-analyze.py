average_age = 0
older_men_name = ''
older_men_age = 0
peoples = 0
how_many_girls_have_less_then_20 = 0
girls = 0
i = 0


try:
    user = int(input("Insert how many people do you want to sign: "))

    for i in range(1,user+1):
        
        print("\n","=-"*5,f"People [{i}]","=-"*5,"\n")

        name = input("Type your name: ")
        age = input("Type your age: ")
        sex = input("Type your sex ([M]ale or [F]emale): ")

        if sex.upper()[0] == 'M' or sex.upper()[0] == "F":
            if sex.upper()[0] == 'M':
                if int(age) > int(older_men_age):
                    
                    older_men_age = age
                    older_men_name = name
            
            if sex.upper()[0] == 'F':
                girls += 1
                if int(age) < 20:
                    how_many_girls_have_less_then_20 += 1
            
            average_age += int(age)
            peoples += 1

        else:
            print("Insert, a valid sex")
            break

    print(f"\nThe average age of the group is [{average_age/peoples}] years old")
    print(f"The older men of the group is [{older_men_name}] with [{older_men_age}] years old")
    print(f"And [{how_many_girls_have_less_then_20}] womans have less then tweenty years\n")
        
except ValueError:
    print("Please, enter a valid value")