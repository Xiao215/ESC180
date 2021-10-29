def sum_nums(L):
  s = 0
  for num in L:
    s += num

  return s

def count_evens(L):
  e = 0
  for num in L:
    if (num%2==0):
        e+=1
  return e
  
if __name__ == '__main__':
    print("even #:",count_evens([x for x in range(100)]))