while True:
 nap = input("Milyen nap van ma?:  ")
 if nap == "hétfő" :
    print("A hét 1. napja,Hétköznap ")
    break
 elif nap == "kedd":
    print("A hét 2. napja,Hétköznap")
    break
 elif nap == "szerda":
    print("A hét 3. napja,Hétköznap")
    break
 elif nap == "csütörtök":
    print("A hét 4. napja,Hétköznap")
    break
 elif nap == "péntek":
    print("A hét 5. napja,Hétköznap")
    break
 elif nap == "szombat":
    print("A hét 6. napja,Hétvége") 
    break
 elif nap == "vasárnap":
    print("A hét 7. napja ,Hétvége")
    break
 else :
    print(" HIBA ")
print("Program vége")