def getList(L1, L2):
    if(len(L2)==1):
        print(L2[0])
        return
    print(L2[0])
    print(L1[len(L1)-1])
    getList(L1[:len(L1)-1], L2[1:])
def zigzag1(L):
    getList(L[:len(L)//2], L[len(L)//2:])
zigzag1([1,2,3,4,5,6,7,8,9,10,11])