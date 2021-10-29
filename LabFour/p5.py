import math
def sig(n):
    counter=0
    while(True):
        if(int(n*(10**counter))==int(math.pi*(10**counter))):
            counter+=1
        else:
            break
    return counter
def formula(n):
    return (((-1.0)**n)/(2.0*n+1))

if __name__ == '__main__':
    n = 10000
    piOverFour=0
    for i in range(n+1):
        piOverFour+=formula(i)
    #3.1415926
    print(sig(piOverFour*4))


    
