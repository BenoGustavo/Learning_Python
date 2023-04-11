import math

angle = float(input('Insert the wished angle: '))

cos = math.cos(math.radians(angle))
Sin = math.sin(math.radians(angle))
Tan = math.tan(math.radians(angle))

print('The ANGLE is {:.2f} and his COS is {:.2f}, and the SIN is {:.2f}, and the TAN is {:.2f}'.format(angle,cos,Sin,Tan))