def is_balanced(s):
    if(s.find("(")==-1 and s.rfind(")")==-1):
        return True
    elif(s.find("(")==-1 or s.rfind(")")==-1):
        return False
    else:
        if(s.find(")")<s.find("(")):
            return False
        elif(s.find(")") < 1+s[s.find("(")+1:].find("(")):
            return is_balanced(s[s.find(")")+1:]) 
        else:
            return is_balanced(s[s.find("(")+1:s.rfind(")")]) 

print(is_balanced("(()())()())"))