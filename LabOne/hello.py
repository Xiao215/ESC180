#Problem 1
print("Hello, Python")
#Problem 2
print("Hello, Maria")
print("Hello, Xiao")
#Problem 3
nameOne="Xiao"
nameTwo="Maria"
print(f"Hello, {nameOne} and {nameTwo}. Your names are {nameOne} and {nameTwo}. Hi there. Your names are still {nameOne} and {nameTwo}.")
#Problem 4
nameOne="Prof. Cluett"
nameTwo="Prof. Thywissen"

#Problem 5
def greeting(str):
    if str=="Lord Voldemort":
        print("I'm not talking to you.")
    else:
        print(f"Hello, {str}")

greetee="Name!!!"
greeting(greetee)
greetee="Lord Voldemort"
greeting(greetee)