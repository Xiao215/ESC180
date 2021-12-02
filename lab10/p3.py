def reverse_rec(L):
    if (len(L)==1): return L
    return [L[len(L)-1]]+reverse_rec(L[:len(L)-1])
print(reverse_rec([1,2,3,4,5,6,7,8]))
