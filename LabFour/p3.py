def lists_are_the_same(list1, list2):
    if(len(list1)!=len(list2)):
        return False
    else:
        for i in range (len(list2)):
            if (list1[i]!=list2[i]):
                return False
        return True
if __name__ == '__main__':
    print (lists_are_the_same([x for x in range(10)],[x for x in range(10)]))
    print (lists_are_the_same([x+1 for x in range(10)],[x for x in range(10)]))
    print (lists_are_the_same([x for x in range(5)],[x for x in range(10)]))