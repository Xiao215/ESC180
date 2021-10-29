def print_matrix_dim(M):
    row=len(M)
    column=len(M[0])
    return str(row)+"x"+str(column)
def mult_M_v(M, v):
    new_vector = [0]*len(M)
    #nxm
    for i in range (len(M)):#n
        sum=0
        for o in range (len(M[i])):
            #m
            sum+=M[i][o]*v[o]
        new_vector[i]=sum
    return new_vector

def mult_M1_M2(M1, M2):
    #nxm mxp
    if(len(M1[0])!=len(M2)): return "can not multiply this matrix"
    new_matrix=[]
    #nxp
    new_matrix=[[0]*len(M2[0])]*len[M1]
    for i in range (len(M1)):
        zeros=[]
        for j in range (len(M2[0])):
            zeros.append(0)
        new_matrix.append(zeros)
    for a in range (len(M1)): #n
        for b in range (len(M2[0])): #p
            sum = 0
            for c in range (len(M1[0])): #m
                sum += M1[a][c]*M2[c][b]
            new_matrix[a][b]=sum
    return new_matrix

if __name__ == '__main__':
    list0=[[1,2],[3,4],[5,6] ]
    list1=[[1,2],[3,4]]
    list2=[[5,6,7],[8,9,10]]
    list3=[[1,2,3],[4,5,6]]
    list4=[7,8,9]
    print(print_matrix_dim(list0))
    print(mult_M1_M2(list1, list2))
    print(mult_M_v(list3, list4))
