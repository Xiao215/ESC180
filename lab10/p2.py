def interleave(l1, l2):
    if(len(l1)==1):
        return [l1[0],l2[0]]
    return [l1[0], l2[0]]+interleave(l1[1:], l2[1:])
print (interleave([1,2,3,4],[5,6,7,8]))