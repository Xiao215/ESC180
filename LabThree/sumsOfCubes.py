def cube(n):
    sum=0
    for i in range(1, n+1):
        sum+= i**3
    return sum
def fancyEquation(n):
    return ((n*(n+1))/float(2))**2
if __name__ == '__main__':
    print('Enter your n here:')
    n = input()
    print('Your sum through sumation:',cube(n))
    print('Your sum through equation:',fancyEquation(n))
    x = cube(n)==fancyEquation(n) and 'equal' or 'not equal'
    print('Two numbers are '+x)
