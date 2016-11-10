#section created by Michael G2.Y on 8/11 To carry out the landing on Mars
#Last modify 2016-10-29-23-23
#@Auther Michael 3778

from lib import*

#----------------------------------1 choice---------------------------------
#launch first
def MarsLanding():
    print("After seven months, seven long, long months...")
    print("your space craft has finally entered the mars orbit")
    print("now, be prepared. will you success or die trying?")
    print("restarting the system")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("System online")
    PeopleSpeaking("System", "System: you may continue your mission, captain.")
    answer = choiceInput("start landing process", "wait a minute")
    if(answer == 1):
        Second()
    elif(answer == 2):
        ThirdOne()
    return

#----------------------------------2 choice---------------------------------
def Second():
    PeopleSpeaking("System","landing process started")
    PeopleSpeaking("Current Location","Mars satellite orbit")
    answer = choiceInput("decelerate","turn the direction of ship 180 degrees")
    if(answer == 1):
        ThirdOne()
    elif(answer == 2):
        ThirdTwo()
    return

#----------------------------------3 choice---------------------------------
def ThirdOne():
    PeopleSpeaking("System","WARNING, you are dropping into mars too fast.")
    PeopleSpeaking("Current Speed","20m/s")
    answer = choiceInput("turn the direction of ship170°","decelerate")
    if(answer == 1):
        ThirdTwo()
    elif(answer == 2):
        ForthOne()
    return

def ThirdTwo():
    PeopleSpeaking("System","turned the direction successfully, entered landing orbit.")
    answer = choiceInput("decelerate","...")
    if(answer == 1):
        ForthOne()
    elif(answer == 2):
        ForthThree()
    return
#----------------------------------4 choice---------------------------------
def ForthOne():
    PeopleSpeaking("System","WARNING, your speed is too fast, space ship lost control.")
    PeopleSpeaking("Current Speed","40m/s")
    answer = choiceInput("what...","what...")
    if(answer == 1):
        FifthOne()
        Second()
    elif(answer == 2):
        FifthOne()
        ForthOne()
    return

def ForthTwo():
    PeopleSpeaking("System","WARNING, breaker is broken.")
    PeopleSpeaking("Current Speed","40m/s")
    answer = choiceInput("what...","what...")
    if(answer == 1):
        FifthTwo()
    elif(answer == 2):
        ForthOne()
    return

def ForthThree():
    PeopleSpeaking("System","WARNING, space ship bottom overheats,")
    PeopleSpeaking("      ","heat-proof layer reaches 1000 degreese")
    answer = choiceInput("open parachute","decelerate")
    if(answer == 1):
        FifthTwo()
    elif(answer == 2):
        FifthThree()
    return

#----------------------------------5 choice---------------------------------
def FifthOne():
    print("failed,your space ship crashed")
    END()
    return

def FifthTwo():
    PeopleSpeaking("System","WARNING, parachute overload")
    answer = choiceInput("close the parachute","do nothing")
    if(answer == 1):
        FifthOne()
        FifthTwo()
    elif(answer == 2):
        SixthOne()
    return

def FifthThree():
    PeopleSpeaking("System","WARNING, parachute overload")
    answer = choiceInput("close the parachute","do nothing")
    if(answer == 1):
        SixthOne()
    elif(answer == 2):
        FifthOne()
        FifthThree()
    return

#----------------------------------6 choice---------------------------------
def SixthOne():
    PeopleSpeaking("System","reaches landing speed, now you can land on mars")
    answer = choiceInput("land","do nothing")
    if(answer == 1):
        SeventhOne()
    elif(answer == 2):
        FifthOne()
        SixthOne()
    return

#----------------------------------7 choice---------------------------------
def SeventhOne():
    PeopleSpeaking("System","Landed successfully")
    PeopleSpeaking("Earth","congratulations,you are the first group of human")
    PeopleSpeaking("     ","beings on mars, you are the pride of all human being")
    return
