def cube(n):
    sum=0
    for i in range(1, n+1):
        sum+= i**3
    return sum
def fancyEquation(n):
    return ((n*(n+1))/float(2))**2
def check_sum(n):
    x = cube(n)==fancyEquation(n) and 'equal' or 'not equal'
    print('Two numbers are '+x)
def check_sums_up_to_n(N):
    for i in range (1, N+1):
        if cube(n)!=fancyEquation(n):
            return False
    return True
if __name__ == '__main__':
    print('Enter your n here:')
    n = input()
    print('Your sum through sumation:',cube(n))
    print('Your sum through equation:',fancyEquation(n))
    check_sum(n)
    print('Enter your N here:')
    N = input()
    if check_sums_up_to_n(N):
        print('for every n less than or equal to N, the formula works')
    else:
        print('formula failed')

