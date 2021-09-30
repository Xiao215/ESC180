import math
def display_current_value(current_value):
    print("Current value:",current_value)
def add(to_add):
    update()
    global current_value
    current_value+=to_add
def devide(to_devide):
    update()
    global current_value
    if to_devide==0:
        print("re-enter")
    else:
        current_value/=float(to_devide)
def substact(to_substract):
    update()
    global current_value
    current_value-=to_substract
def multiply(to_multiply):
    update()
    global current_value
    current_value*=to_multiply
def memory():
    global current_value
    global memoryVal
    memoryVal=current_value
def restore():
    update()
    global current_value
    global memoryVal
    current_value=memoryVal
def update():
    global current_value
    global lastVal
    lastVal=current_value
def undo():
    global current_value
    global lastVal
    current_value+=lastVal
    lastVal=current_value-lastVal
    current_value-=lastVal

def get_current_value():
    return current_value

def initialize():
  global astVal
  astVal=-1
  global current_value
  current_value = 0
  global memoryVal
  memoryVal=-1
if __name__ == "__main__":
  initialize()
  print("Welcome")
  display_current_value(current_value)
  add(11)
  display_current_value(current_value)    
  devide(12)
  display_current_value(current_value)    
  substact(127)
  display_current_value(current_value)
  multiply(math.pi)
  display_current_value(current_value)
  memory()
  display_current_value(current_value)
  devide(math.e)
  display_current_value(current_value)
  restore()
  display_current_value(current_value)
  undo()
  display_current_value(current_value)


