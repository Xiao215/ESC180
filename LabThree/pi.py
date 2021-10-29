def formula(n):
    return (((-1.0)**n)/(2.0*n+1))

if __name__ == '__main__':
    n = 10000
    piOverFour=0
    for i in range(n+1):
        piOverFour+=formula(i)
    print('pi is:',piOverFour*4)
