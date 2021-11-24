def initialize():
    """
    initialize all the global variable here
    """
    #health represents the total health points
    global health
    health = 0
    #hedons represents the total hedons points
    global hedons
    hedons = 0
    #running time represent how long has the person been running.
    #this variable will be refresh to 0 everything the person do things
    #other than running
    global running_time
    running_time = 0
    #star box will contain all the star requested in the most recent 2h
    global star_box
    star_box= []
    #star used is a place holder to store the information of
    #whether the requested star is avaliable to use, as well as
    #which activity should it be used for
    #The index 0 refers to whether the star 
    #has been used (True) or is avaliable to use (False)
    #The index 1 refers to the activity type and will be None if the star has been used
    global star_used
    star_used = [True, None]
    #the time cool down (max 2h) to make the person not tired again
    global tired_duration
    tired_duration = 0
    #showing whether the player get bored or not
    global bored
    bored = False
def offer_star(activity):
    """
    activity: the name of the activity that the player wants to get star for

    This function will offer the user a star to a specifc activity that they want
    """
    global bored
    if bored: return
    global star_box
    global star_used
    if len(star_box)==2:
        bored = True
    else:
        star_box.append(120)
        star_used=[False, activity]
def check_star(minute):
    """
    minute: the time elapes for the specific event to happen

    This function will update the time for each star,
    counting down from 120s to 0s
    """
    if bored: return
    global star_box
    #delete each time in the list by the minute elapes
    #if the time comes to negative or 0, it will be automatically opt out
    star_box = [x-minute for x in star_box if x-minute>0]
def running_hedons(minute):
    """
    minute: the time elapes for running

    This function will take the minute of running, and calculate the change in hedons
    """
    global hedons
    if tired_duration == 0:
        if minute <=10:
            hedons += 2* minute
        else:
            hedons += 4*10 - 2*(minute)
    else:
        hedons -= 2*minute
def running_health(minute):
    """
    minute: the time elapes for running

    This function will take the minute of running, and calculate the change in health
    """
    global health
    if minute+running_time <=180:
        health+=3*minute
    elif running_time<180:
        health += (running_time+minute-180) + 3 * (180-running_time)
    else:
        health += minute
def carrying_health(minute):
    """
    minute: the time elapes for carrying textbook

    This function will take the minute of running, and calculate the change in health
    """
    global health
    health +=  minute*2
def carrying_hedons(minute):
    """
    minute: the time elapes for carrying textbook

    This function will take the minute of running, and calculate the change in hedons
    """
    global hedons
    if tired_duration == 0:
        if minute <=20:
            hedons += minute
        else: 
            hedons += 40 - (minute)
    else:
        hedons -= 2*minute
def perform_activity(activity, minute):
    """
    minute: the time elapes for the specific activity
    activity: the name or the type of the activity

    This function will be called and perform the specific activity as indicated
    """
    global running_time
    global tired_duration
    global star_used
    global hedons
    if activity == "running":
        running_health(minute)
        running_hedons(minute)
        running_time += minute
        #set the cool down of the tiredness back to 2h which is 120 minutes
        tired_duration = 120 
    elif activity == "textbooks":
        carrying_health(minute)
        carrying_hedons(minute)
        #set the cool down of the tiredness back to 2h which is 120 minutes
        tired_duration = 120 
        running_time = 0
    elif activity == "resting":
        tired_duration -= minute
        if tired_duration < 0:
            tired_duration = 0
        running_time = 0
    else:
        print("invalid activity name")

    #the following if loop will check if a star was just offered
    if (not star_used[0]):
        #a star is offered, check if it's related to this current activity
        if (star_used[1] == activity):
            increment = minute<=10 and minute*3 or 30
            hedons += increment
        #turn the star information back to already used status
        star_used = [True, None]
    check_star(minute)

def get_cur_hedons():
    """
    get the current hedons
    """
    return hedons
def get_cur_health():
    """
    get the current health point value
    """
    return health
def most_fun_activity_minute():
    """
    return the activity that will have the highest hedon return in 1 min
    """
    global star_used
    if(tired_duration==0):
        # if player is not tired, the activity would only be between textbook and running
        return star_used[1]=="textbooks" and "textbook" or "running"
    else:
        # if no star is giving, rest is the best option, otherwise, it will be the activity
        #that is offered a star
        if star_used[1] == None:
            return "resting"
        else: return star_used[1]
def star_can_be_taken(activity):
    """
    return whether the activity can take a star if it is done right after
    """
    return (not star_used[0]) and activity == star_used[1] 
if __name__ == '__main__':
    initialize()
    print(most_fun_activity_minute())
    perform_activity("running", 10)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    print(most_fun_activity_minute())
    print(most_fun_activity_minute())
    offer_star("running")
    perform_activity("running", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 10)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    offer_star("running")
    perform_activity("running", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 70)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    perform_activity("running", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 50)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    perform_activity("resting", 140)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    offer_star("textbooks")
    perform_activity("textbooks", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    perform_activity("running", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())