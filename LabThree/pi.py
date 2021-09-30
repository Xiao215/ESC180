def formula(n):
    return (((-1.0)**n)/(2.0*n+1))

if __name__ == '__main__':
    print("How many n do you want to run?")
    n = 999999999
    piOverFour=0
    for i in range(n+1):
        piOverFour+=formula(i)
    print('pi is:',piOverFour*4)
