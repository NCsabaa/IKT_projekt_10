import os
import time
import random

def clear():
    os.system('CLS')

dobas=int(input("Hányszor dobsz? "))
clear()
for ismetles in range (dobas):
    x=random.randint(1,7)
    if ismetles == 1:
         print(r"""
         _________
        /        /|
       /_______ / |
       |       |  |
       |   o   | /
       |_______|/  """)
    elif ismetles == 2:
        print(r"""
         _________
        /        /|
       /_______ / |
       |       |  |
       | o  o  | /
       |_______|/ """)

    elif ismetles == 3:
        print(r"""
         _________
        /        /|
       /_______ / |
       |     o |  |
       |   o   | /
       |_o_____|/ """)

    elif ismetles == 4:
        print(r"""
         _________
        /        /|
       /_______ / |
       | o   o |  |
       |       | /
       |_o___o_|/ """)

    elif ismetles == 5:
        print(r"""
  
          ________
        /        /|
       /_______ / |
       | o   o |  |
       |   o   | /
       |_o___o_|/ """)

    elif ismetles == 6:
        print(r"""
         _________
        /        /|
       /_______ / |
       | o   o |  |
       | o   o | /
       |_o___o_|/  """)
    time.sleep(2)
    clear()
