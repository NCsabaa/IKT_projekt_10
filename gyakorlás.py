nev=input("Felhasználó neve: ")

print("Üdvözöljük", nev)

print("**********\n\noooooooooo")

print("*o*o*o*o*o\n*o*o*o*o*o")

szam1=int (input("Adj meg egy számot: "))

szam2=int (input("Adj meg még egy számot: "))

szam3=int (input("Add meg a harmadik számot: "))

muvelet=input("Kérek egy műveletet: ")

if (muvelet== "*"):

    print(szam1*szam2)

elif (muvelet=="+"):

    print(szam1+szam2+szam3)
elif (muvelet=="-"):

    print(szam1-szam2)

elif (muvelet=="/"):

    print(szam1/szam2)

else:
    print("hiba")
