from os import system
from time import sleep
system("clear")
print("enter limit")
lim = int(input())
system("clear")
for i in range(1, lim+1):
    print(i)
    sleep(1)
