from os import system
import random

def loop():
    w=180
       
    print(' '*w)

    for height in range(60):
        print(' ',end='')
        r=random.randrange(2,175)
        for i in range(180):
            print(" ",end='')
            
            if(i==r):
                g=178-i
                print("i",end='')
                print(" "*g,end='')
                r=-1
                break

        print(" ")
       
        
    print(' '*w)
    system("clear")
        
while(1):

    loop()
