x=int(input("Kérek egy számot: "))
y=int(input("Kérek még egy  számot: "))
z=int(input("Kérek egy harmadik számot: "))

if (x<y and x<z):
    print("Az eső szám a legkisebb")

elif (y<x and y<z):
    print("A második szám a legkisebb")

elif (z<x and z<y):
    print("A harmadik szám a legkisebb")

elif (x==y==z):
    print("A számok egyenlőek")

else:
    print("Hiba")

