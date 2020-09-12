from os import system
import random
from time import sleep


t = 1
f = 0
c = 0
r = 0

x = 0
y = 0

def loop():
    global r,f,c,x,y
    
    w=62
    f = 0
    if(f ==  0):
        if(r == 0 ):
            
            r=random.randrange(1,30)
            
        elif(c==10):
            r=random.randrange(5,30)
            f = 1
            

    #top line  

    print('#'*w)
    #height line
    for height in range(2,32):
        print('#',end='')
        #r=random.randrange(2,55)
        for i in range(2,62):
            print(" ",end='')
            
            if(r==height and r==i or f==1):
                x = height
                y = i
                g=60-i #prints character and prints remaining spaces
                print("i",end='')
                print(" "*g,end='')
                r=-1
                f= 2
                break
            elif(x == height and y == i):
                g=60-i #prints character and prints remaining spaces
                print("i",end='')
                print(" "*g,end='')
                r=-1
                f= 2
                break


        print("#")
        #sleep(0.3)
    #bottom line
    print('#'*w)
    

def main():
    global t
    global c
    global r
    while(t):
        
        
        #t=t-1
        loop()
        sleep(0.3)
        system("cls")
        c+=1

main()