import numpy as np

"""
# Printing matrices using NumPy:

# Convert a list of lists into an array:
M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
M = np.array(M_listoflists)
# Now print it:
print(M)

"""


#Compute M*x for matrix M and vector x by using
#dot. To do that, we need to obtain arrays
#M and x
MM = np.array([[0,0,1,0,2],[1,0,2,3,4],[3,0,4,2,1],[1,0,1,1,2]])


# To obtain a list of lists from the array M, we use .tolist()
M_listoflists = MM.tolist() 

print(M_listoflists) #[[1, -2, 3], [3, 10, 1], [1, 5, 3]]


def print_matrix(M_lol):
    string="[["
    for i in range(len(M_lol)):
        if(i!=0): string+="\n ["
        string+=str(M_lol[i][0])
        for j in range(1,len(M_lol[0])):
            string+=" "
            string+=str(M_lol[i][j])
        string+="]"
    string+="]"
    print(string)
def get_lead_ind(row):
    for i in range (len(row)):
        if row[i]!=0:
            return i
    return len(row)
def get_row_to_swap(M, start_i):
    if (get_lead_ind(M[start_i])==start_i): return start_i
    max_left=start_i
    #row number
    for i in range (len(M)-1,start_i, -1):
        if get_lead_ind(M[i])<get_lead_ind(M[max_left]):
            max_left=i
        if (get_lead_ind(M[i])==start_i):
            L=M[start_i]
            M[start_i]=M[i]
            M[i]=L
            return i
    L=M[start_i]
    M[start_i]=M[max_left]
    M[max_left]=L
    return max_left

def add_rows_coefs(r1, c1, r2, c2):
    return [c1*a+c2*b for a, b in zip(r1, r2)]
    #NEW STUFF!
def eliminate(M, row_to_sub, best_lead_ind):
    if(M[row_to_sub][best_lead_ind]!=0):
        for i in range (row_to_sub+1, len(M)):#3
            #len(M)
            frac=M[i][best_lead_ind]/M[row_to_sub][best_lead_ind]
            M[i]=[a-frac*b==int(a-frac*b) and int(a-frac*b) or a-frac*b for a, b in zip(M[i], M[row_to_sub])]
def eliminate1(M, row_to_sub, best_lead_ind):
    if(M[row_to_sub][best_lead_ind]!=0):
        for i in range (row_to_sub):#3
            #len(M)
            frac=M[i][best_lead_ind]/M[row_to_sub][best_lead_ind]
            M[i]=[a-frac*b==int(a-frac*b) and int(a-frac*b) or a-frac*b for a, b in zip(M[i], M[row_to_sub])]
def deviding(M):
    for i in range (len(M)):
        if(get_lead_ind(M[i])!=len(M[i])):
            M[i]=[a/M[i][get_lead_ind(M[i])]==int(a/M[i][get_lead_ind(M[i])]) and int(a/M[i][get_lead_ind(M[i])]) or a/M[i][get_lead_ind(M[i])] for a in M[i]]

def forward_step(M):
    print("The matrix is currently:")
    print_matrix(M)
    for r in range (len(M)):
        print(f"Now looking at row {r}")
        print(f"Swapping rows {r} and {get_row_to_swap(M, r)} so that entry {get_lead_ind(M[r])} in the current row is non-zero")
        print("The matrix is currently:")
        print_matrix(M)
        eliminate(M, r, r)
        print(f"Adding row {r} to rows below it to eliminate coefficients in column {get_lead_ind(M[r])}")
        print("The matrix is currently:")
        print_matrix(M)
    print("================================================================================")   
    print("Done with the forward step")
    print("The matrix is currently:")
    print_matrix(M)
def backward_step(M):
    print("================================================================================")   
    print("Now performing the backward step")
    for r in range (len(M)-1, -1, -1):
        eliminate1(M, r, r)
        print(f"Adding row {r} to rows above it to eliminate coefficients in column {r}")
        print("The matrix is currently:")
        print_matrix(M)
    print("================================================================================")
    print("Now dividing each row by the leading coefficient")
    print("The matrix is currently:")
    deviding(M)
    print_matrix(M)
    
forward_step(M_listoflists)
backward_step(M_listoflists)



"""
print("\n\n\n---------CUT----------\n\n\n")
#Compute M*x for matrix M and vector x by using
#dot. To do that, we need to obtain arrays
#M and x

MMM = np.array([[1,-2,3],[3,10,1],[1,5,3]])
x = np.array([75,10,-11])
MMMM=MMM.tolist() 
forward_step(MMMM)
backward_step(MMMM)
MMM = np.array(MMMM)
b = np.matmul(MMM,x)   
print_matrix(b.tolist())
"""