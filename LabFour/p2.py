def list_to_str(lis):
    string ="["
    comma =False
    for num in lis:
        if not comma:
            comma=True
        else:
            string+=", "
        string+=str(num)
    string += "]"
    return string

if __name__ == '__main__':
    print (list_to_str([x for x in range(10)]))