def match_pattern(list1, list2):
    if len(list1)<len(list2): return False
    for i in range(len(list1)-len(list2)):
        if(list1[i:i+len(list2)]==list2):
            return True
    return False
if __name__ == '__main__':
    list1=[1,2,3,4,5]
    list2=[2,4]
    print(match_pattern(list1, list2))