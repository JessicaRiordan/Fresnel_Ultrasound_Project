from machine import Pin
import time

step = Pin(2, Pin.OUT)                        # Set up Step pin
dir = Pin(3, Pin.OUT)                         # Set up Direction pin
limitsensor=Pin(9, Pin.IN, Pin.PULL_UP)

mircostepM1=Pin(8, Pin.OUT)
mircostepM2=Pin(7, Pin.OUT)
mircostepM3=Pin(6, Pin.OUT)

mircostepM1.value(1)
print(mircostepM1.value())
mircostepM2.value(1)
mircostepM3.value(0)
#def microstepoff():
#    mircostepM1.value(0)
#    mircostepM2.value(0)
#    mircostepM3.value(0)

    
maxsteps=200000

initialised=False
initialising=False

currentpos=0

def stepp(direction):
    dir.value(direction)
    steptime=200
    step.value(0)
    time.sleep_us(steptime)
    step.value(1)
    time.sleep_us(steptime)


def initialise():
    global initialising
    global initialised
    global maxsteps
    global currentpos
    
    currentcount=0
    
    initialising=True
    print(initialising)
    print(f"limit sensor={limitsensor.value()}")
    print(f"count={currentcount}")
    while limitsensor.value() and currentcount<maxsteps:
        currentcount+=1
        move(1,1)
    print(f"count={currentcount}")    
    initialising=False
    print(initialising)
    if currentcount<maxsteps:
        initialised=True
        currentpos=0
    while not limitsensor.value():
        stepp(0)
    return False

def atlimit():
    if limitsensor.value():
        return False
    
def getcurrentpos():
    global currentpos
    return currentpos

def move(target_steps,directionAway):
    global initialising
    global initialised
    global maxsteps
    global currentpos
    
    if not initialised and not initialising:
        print(initialised)
        print(initialising)
        return "Not Initialised!"
        
    counter = 0
    dir.value(directionAway)                              # 0 Towards Motor, 1 Away From Motor
    steptime=200                        #will not move with steptime 200us if not microstepping
    
    if currentpos + target_steps > maxsteps and not directionAway:
        return "Too Far"
        
    if directionAway:
        currentpos -= target_steps
    else:
        currentpos += target_steps
    
    while counter < target_steps:    # At 1/16th microstepping
        if not limitsensor.value():
            initialised=False
            currentpos=0
            return "At Limit"
      
        counter = counter + 1
        stepp(directionAway)
        
           