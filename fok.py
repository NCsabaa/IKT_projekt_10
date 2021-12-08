def temp(c):
    if c > 100 :
        print("forr")
    elif c == 100:
        print("forráspont")
    elif  c >40:
        print("forró")
    elif c==40:
        print("meleg")
    elif c==20:
        print("normális")
    elif c==0:
        print("fagypont")
    elif c<0:
        print("fagy")
for c in reversed(range(-20,121,20)):
    print(c,end="")
    print("°C ->", end="")
    temp(c)
