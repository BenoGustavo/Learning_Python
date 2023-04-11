height = float(input('How big is you wall?: '))
width = float(input("What's the width of your wall?: "))

sqrmeters = height * width
#a cada 2 metros quadrados de parede precisa de 2 litros de tinta
tint = sqrmeters/2

print("Your wall is {} big, and you will need {} liters of tint for painting it".format(sqrmeters,tint))