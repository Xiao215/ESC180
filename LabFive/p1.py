def list1_starts_with_list2(list1, list2):
    if len(list1)<len(list2): return False
    for i in range(len(list2)):
        if list1[i]!=list2[i]: return False
    return True
def list1_starts_with_list2_2(list1, list2):
    if len(list1)<len(list2): return False
    list1=list1[:len(list2)]
    return list2==list1
if __name__ == '__main__':
    list1=[1,2,3,4]
    list2=[3,2,1]
    print(list1_starts_with_list2(list1, list2))
    print(list1_starts_with_list2_2(list1, list2))
