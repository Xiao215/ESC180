import math
def simplify_fraction(a,b):
    counter=0
    for i in range (2+int(math.sqrt(min(a,b))),1,-1):
        counter+=1
        print("i:",i)
        if (a%i==0 and b%i==0):
            a=a/i
            b=b/i
    print("counter for mine:",counter)
    print(a,"/",b)
    
def euclid(a,b,counter,oga, ogb):
    if counter==0:
        oga=a
        ogb=b
    big=max(a,b)
    small=min(a,b)
    counter+=1
    if(big%small==0):
        print("counter for Eulen:",counter)
        print(oga//(small),"/",ogb//(small))
    else:
        euclid(small,big%small,counter,oga,ogb)
def mathGCD(a,b):
    print(a//math.gcd(a,b),"/",b//math.gcd(a,b))
if __name__ == '__main__':
    simplify_fraction(2322,654)
    euclid(2322,654,0, 0, 0)