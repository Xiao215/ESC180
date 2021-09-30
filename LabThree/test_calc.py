import calculator
#how to import calculator if it's in folder lab 2?
#what does if __name__ == '__main__': do
if __name__ == '__main__':
    calculator.initialize()
    calculator.add(42)
    if calculator.get_current_value() == 42:
      print("Test 1 passed")
    else:
      print("Test 1 failed")