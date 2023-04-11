def imc_function(height,weight):
    imc = weight / (height*height)
    return int(imc)


while True:
    height = (input("Insert your height in meters: "))
    weight = (input("Insert your weight: "))
    
    try:
        if float(height).is_integer():
            height = float(height) / 100

        print("\n")

        imc = imc_function(float(height),float(weight))
        break
    except ValueError:
        print("Please, insert a valid value...")
        continue
    

if imc < 16:
    print(f"You need to gain weight immediatly || IMC of {imc:.2f}")

elif imc >= 16 and imc < 17:
    print(f"You need to gain weight || IMC of {imc:.2f}")

elif imc >= 17 and imc < 18.5:
    print(f"You need to gain a little bit of weight || IMC of {imc:.2f}")

elif imc >= 18.5 and imc < 25:
    print(f"You are healty || IMC of {imc:.2f}")

elif imc >= 25 and imc < 30:
    print(f"You are overweight || IMC of {imc:.2f}")

elif imc >= 30 and imc < 35:
    print(f"You are with obese level 1 || IMC of {imc:.2f}")

elif imc >= 35 and imc < 40:
    print(f"You are with obese level 2 || IMC of {imc:.2f}")

elif imc >= 40:
    print(f"You are with severe obese level 3 || IMC of {imc:.2f}")
