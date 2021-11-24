import gamify

#### Running health tests ####
def test_1():
    gamify.initialize()
    gamify.perform_activity("running", 150)
    gamify.perform_activity("running", 50)
    if gamify.get_cur_health() == 560 :
        print("test 1.1 pass")
    else:
        print("test 1.1 fail")

    gamify.initialize()
    gamify.perform_activity("running", 180)   
    if gamify.get_cur_health() == 540 :
        print("test 1.2 pass")
    else:
        print("test 1.2 fail")
    gamify.initialize()
    gamify.perform_activity("running", 200)
    if gamify.get_cur_health() == 560 :  #540+20=560
        print("test 1.3 pass")
    else:
        print("test 1.3 fail")

def test_2():
    gamify.initialize()
    gamify.perform_activity("running", 150)
    gamify.perform_activity("textbooks", 1)
    gamify.perform_activity("running", 50)
    if gamify.get_cur_health() == 602 :
        print("test 2 pass")
    else:
        print("test 2 fail")

def test_3():
    gamify.initialize()
    gamify.perform_activity("running", 150)
    gamify.perform_activity("resting", 1)
    gamify.perform_activity("running", 50)
    if gamify.get_cur_health() == 600 :
        print("test 3 pass")
    else:
        print("test 3 fail")

#### Running hedon tests ####

# Not tired & No Star
def test_4():
    gamify.initialize()
    gamify.perform_activity("running", 10)
    if gamify.get_cur_hedons() == 20 :
        print("test 4.1 pass")
    else:
        print("test 4.1 fail")
    gamify.perform_activity("running", 10)
    if gamify.get_cur_hedons() == 0 :
        print("test 4.2 pass")
    else:
        print("test 4.2 fail")

#### textbooks hedon tests ####

# Not tired & No Star
def test_5():
    gamify.initialize()
    gamify.perform_activity("textbooks", 20)
    if gamify.get_cur_hedons() == 20 :
        print("test 5.1 pass")
    else:
        print("test 5.1 fail")
    gamify.initialize()
    gamify.perform_activity("textbooks", 21)
    if gamify.get_cur_hedons() == 19 :
        print("test 5.2 pass")
    else:
        print("test 5.2 fail")
#Tired & No Star
    gamify.initialize()
    gamify.perform_activity("textbooks", 20) #hedon = 20
    gamify.perform_activity("running", 5)    #hedon = 20-5*2 = 10
    if gamify.get_cur_hedons() == 10 :
        print("test 5.3 pass")
    else:
        print("test 5.3 fail")
#### Rest tests ####
def test_6():
    gamify.initialize()
    gamify.perform_activity("textbooks", 20)
    gamify.perform_activity("resting", 120)
    gamify.perform_activity("textbooks", 20)
    if gamify.get_cur_hedons() == 40 :
        print("test 6.1 pass")
    else:
        print("test 6.1 fail")

##### Star tests #####
def test_7():
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("running", 10)
    if gamify.get_cur_hedons() == 50 :
        print("test 7.1 pass")
    else:
        print("test 7.1 fail")

    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 10)
    if gamify.get_cur_hedons() == 40 :
        print("test 7.1 pass")
    else:
        print("test 7.1 fail")

#bored star test#
def test_8():
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("running", 10)    #hedon 50=10*2+10*3
    if gamify.get_cur_hedons() == 50 :
        print("test 8.1 pass")
    else:
        print("test 8.1 fail")

    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 10)  #hedon 60=50+10*(3-2)
    if gamify.get_cur_hedons() == 60 :
        print("test 8.2 pass")
    else:
        print("test 8.2 fail")

    gamify.offer_star("running")
    gamify.perform_activity("running", 10)    #bored hedon 40=60+10*(-2)
    if gamify.get_cur_hedons() == 40 :
        print("test 8.3 pass")
    else:
        print("test 8.3 fail")

def test_9():

    gamify.initialize()

    gamify.offer_star("running")#0
    gamify.perform_activity("running", 60)    #hedon -50=10*2+10*3-50*2
    if gamify.get_cur_hedons() == -50 :
        print("test 9.1 pass")
    else:
        print("test 9.1 fail")

    gamify.offer_star("textbooks")#60
    gamify.perform_activity("textbooks", 40)
    if gamify.get_cur_hedons() == -100 :
        print("test 9.2 pass")
    else:
        print("test 9.2 fail")

    gamify.perform_activity("resting", 20)
    gamify.offer_star("running") #120
    gamify.perform_activity("running", 10)    # hedon -90=-100+10*(3-2)
    if gamify.get_cur_hedons() == -90 :
        print("test 9.3 pass")
    else:
        print("test 9.3 fail")

def test_10():
    gamify.initialize()
    gamify.offer_star("running") #0
    gamify.perform_activity("running", 60)    #hedon -50=10*2+10*3-50*2
    gamify.offer_star("textbooks") #60
    gamify.perform_activity("textbooks", 40)
    gamify.perform_activity("resting", 20)
    gamify.offer_star("running") #120
    gamify.perform_activity("running", 10)    #hedon -90=-100+10*(3-2)
    gamify.perform_activity("resting", 80)
    gamify.offer_star("textbooks") #210
    gamify.perform_activity("textbooks", 10)  #hedon -80=-100+10*(3-2)
    if gamify.get_cur_hedons() == -80 :
        print("test 10.1 pass")
    else:
        print("test 10.1 fail")

def test_13():
    gamify.initialize()
    gamify.offer_star("running") #0   useless   #activity!=activity test#
    gamify.perform_activity("textbooks", 10)  #hedon 10
    if gamify.get_cur_hedons() == 10 :
        print("test 13.1 pass")
    else:
        print("test 13.1 fail")
    gamify.offer_star("running")#10
    gamify.perform_activity("running", 10)  #hedon 20=10+10*(3-2)
    if gamify.get_cur_hedons() == 20 :
        print("test 13.2 pass")
    else:
        print("test 13.2 fail")

    gamify.offer_star("running")#20
    gamify.perform_activity("running", 10)  #hedon 0=20-10*2
    if gamify.get_cur_hedons() == 0 :
        print("test 13.3 pass")
    else:
        print("test 13.3 fail")


#activity=!activity star test#
def test_14():
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 10)  #star not taken #hedon 20 = 10*2
    if gamify.get_cur_hedons() == 20 :
        print("test 14.1 pass")
    else:
        print("test 14.1 fail")

#not imediately used star test#
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("resting", 10)
    gamify.perform_activity("running", 10)  #star not taken #hedon 20 = 10*2
    if gamify.get_cur_hedons() == 20 :
        print("test 14.2 pass")
    else:
        print("test 14.2 fail")

    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 10)    #hedon 0 = 20-10*2 #tired
    gamify.perform_activity("textbooks", 10)  #star not taken  #hedon -20 = 0-10*2 #tired
    if gamify.get_cur_hedons() == -20 :
        print("test 14.3 pass")
    else:
        print("test 14.3 fail")

##### most fun activity test #####
#tired = rest

def test_11():
    gamify.initialize()
    print(gamify.most_fun_activity_minute()) #running#  #running 2     textbook 1      resting 0

    gamify.perform_activity("resting", 20)
    print(gamify.most_fun_activity_minute()) #running#  #running 2     textbook 1      resting 0

    gamify.perform_activity("running", 1)#tired
    print(gamify.most_fun_activity_minute()) #resting#  #running -2    textbook -2     resting 0

    gamify.perform_activity("textbooks", 1)#tired
    print(gamify.most_fun_activity_minute()) #resting#  #running -2    textbook -2     resting 0

    gamify.offer_star("running")#tired
    print(gamify.most_fun_activity_minute()) #running#  #running 1    textbook -2      resting 0

    gamify.perform_activity("resting", 20)
    gamify.offer_star("textbooks")#tired
    print(gamify.most_fun_activity_minute()) #textbooks#  #running -2    textbook 1      resting 0

    gamify.initialize()
    gamify.offer_star("textbooks")
    print(gamify.most_fun_activity_minute()) #textbooks#  #running 2    textbook 3      resting 0

    gamify.initialize()
    gamify.perform_activity("resting", 20)
    gamify.most_fun_activity_minute()   
    gamify.perform_activity("running", 10)  #hedon 20=10*2
    if gamify.get_cur_hedons() == 20 :
        print("test 11.1 pass")
    else:
        print("test 11.1 fail")

    gamify.initialize()
    gamify.offer_star("running")
    gamify.most_fun_activity_minute()
    gamify.perform_activity("running", 10) #hedon 50=10*(3+2)
    if gamify.get_cur_hedons() == 50 :
        print("test 11.2 pass")
    else:
        print("test 11.2 fail")


def test_12():
    gamify.initialize()
    gamify.perform_activity("running", 5)   #hedon 10=5*2   health 15=5*3
    print(gamify.most_fun_activity_minute()) 
    if gamify.get_cur_health() == 15 :
        print("test 12.1 pass")
    else:
        print("test 12.1 fail")
    if gamify.get_cur_hedons() == 10 :
        print("test 12.2 pass")
    else:
        print("test 12.2 fail")

##### star can tmd be taken #####
def test_cnm():
    gamify.initialize()
    gamify.offer_star("textbooks")
    #activity = activity & not bored & immediatly used
    if gamify.star_can_be_taken("textbooks") == True :
        print("test cnm.1 pass")
    else:
        print("test cnm.1 fail")

    #activity =! activity
    if gamify.star_can_be_taken("running") == False :
        print("test cnm.2 pass")
    else:
        print("test cnm.2 fail")

    if gamify.star_can_be_taken("resting") == False :
        print("test cnm.3 pass")
    else:
        print("test cnm.3 fail")

    gamify.initialize()
    #star not offered
    if gamify.star_can_be_taken("textbooks") == False :
        print("test cnm.4 pass")
    else:
        print("test cnm.4 fail")

    if gamify.star_can_be_taken("running") == False :
        print("test cnm.5 pass")
    else:
        print("test cnm.5 fail")

    if gamify.star_can_be_taken("resting") == False :
        print("test cnm.6 pass")
    else:
        print("test cnm.6 fail")

    gamify.initialize()
    #not imediately used
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 10)
    if gamify.star_can_be_taken("textbooks") == False :
        print("test cnm.7 pass")
    else:
        print("test cnm.7 fail")

    gamify.offer_star("running")
    gamify.perform_activity("resting", 10)
    if gamify.star_can_be_taken("running") == False :
        print("test cnm.8 pass")
    else:
        print("test cnm.8 fail")

    gamify.initialize()
    #bored
    gamify.offer_star("textbooks")             #star offtered & not taken
    gamify.perform_activity("resting", 10)
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 10)
    gamify.offer_star("textbooks")
    if gamify.star_can_be_taken("textbooks") == False :
        print("test cnm.9 pass")
    else:
        print("test cnm.9 fail")

    gamify.initialize()
    gamify.offer_star("textbooks")             #star offtered & taken
    gamify.perform_activity("textbooks", 10)
    gamify.offer_star("running")               #star offtered & taken
    gamify.perform_activity("running", 10)
    gamify.offer_star("textbooks")             #star offtered & bored
    if gamify.star_can_be_taken("textbooks") == False :
        print("test cnm.10 pass")
    else:
        print("test cnm.10 fail")

def test_wdnmd():
    gamify.initialize()
    gamify.perform_activity("resting", 20)
    gamify.star_can_be_taken("textbooks")
    gamify.perform_activity("running", 10)  #hedon 20=10*2
    if gamify.get_cur_hedons() == 20 :
        print("test wdnmd.1 pass")
    else:
        print("test wdnmd.1 fail")

    gamify.initialize()
    gamify.offer_star("running")
    gamify.star_can_be_taken("textbooks")
    gamify.perform_activity("running", 10) #hedon 50=10*(3+2)
    if gamify.get_cur_hedons() == 50 :
        print("test wdnmd.2 pass")
    else:
        print("test wdnmd.2 fail")


if __name__=='__main__':
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    test_7()
    test_8()
    test_9()
    test_10()
    test_11()
    test_12()
    test_13()
    test_14()
    test_cnm()
    test_wdnmd()
