from os import system
from time import sleep
h = 0
m = 0
s = 0
while(h != 24):
    sleep(1)
    system("cls")
    print(str(h) + ":" + str(m) + ":" + str(s))
    s += 1
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0
