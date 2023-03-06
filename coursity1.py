#This is a program to calculate the cosine and degrees of an angle given the coordinates of 2 points in a Cartesian coordinate system.
#a1 and a2 represent the x and y of a point in the first line respectively
#b1 and b2 represent the x and y of a point in the second line respectively
import math

a1 = float(input('a1 = '))
a2 = float(input('a2 = '))
b1 = float(input('b1 = '))
b2 = float(input('b2 = '))

print(a1, a2, b1,b2)

arithmitis = ((a1*b1) + (a2*b2))

paronomastis = math.sqrt(a1**2 + a2**2) * math.sqrt(b1**2 + b2**2)

costh = arithmitis / paronomastis
goniath = math.degrees(math.acos(costh))

print("The cosine is", costh, " rad")
print("The angle is ", goniath, " degrees")