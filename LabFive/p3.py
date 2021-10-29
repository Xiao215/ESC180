def repeats(list0):
    if(len(list0)==0 or len(list0)==1): return False
    placeholder = list0[0]
    for i in range (1, len(list0)):
        if list0[i]==placeholder: return True
        placeholder=list0[i]
    return False
if __name__ == '__main__':
    list0=[]
    print(repeats(list0))