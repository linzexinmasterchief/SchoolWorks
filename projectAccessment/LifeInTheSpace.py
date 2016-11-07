#Last modify 2016-10-29-23-23

from lib import*

#----------------------------------1 choice---------------------------------
#launch first
def InSpace():
    PeopleSpeaking("System", "Now you have successfully entered the orbit,")
    PeopleSpeaking("Scientist"," the AI Clark will be there to help you make your choice.")
    PeopleSpeaking(" ", "At this time your feel very hungry")
    answer = choiceInput("eat now", "wait some time when feel so hungry")
    if(answer == 1):
        #good
        PeopleSpeaking("Clark","good choice")
        SecondOne()
    elif(answer == 2):
        #dead
        PeopleSpeaking("Clark","you have been too hungry to move,")
        PeopleSpeaking("     "," starved to death in the spaceship")
        END()
        InSpace()
    return

#----------------------------------2 choice---------------------------------
#launch second
def SecondOne():
    PeopleSpeaking("System", " you have a piece of golden tempting cookies")
    PeopleSpeaking("      ", " and a lump of green paste, you will choose")
    answer = choiceInput("cookie", "paste")
    if(answer == 2):
        #good
        PeopleSpeaking("Clark","good choice")
        ThirdOne()
    elif(answer == 1):
        #dead
        PeopleSpeaking("Clark","eat biscuits and the powder will float to everywhere,")
        PeopleSpeaking("     ","other people will be accidentally inhaled, you are not a good astronaut")
        END()
        SecondOne()
    return

#----------------------------------3 choice---------------------------------
#launch third
def ThirdOne():
    PeopleSpeaking("System", "Your water level went down, you want to: ")
    answer = choiceInput("drink water with straw", "use cups to drink")
    if(answer == 1):
        #good
        PeopleSpeaking("Clark","although seems foolish, but it is a wise choice")
        ForthOne()
    elif(answer == 2):
        #dead
        PeopleSpeaking("Clark","water floating to everywhere, damaged the spacecraft.")
        END()
        ThirdOne()
    return

#----------------------------------4 choice---------------------------------
#launch forth
def ForthOne():
    PeopleSpeaking("System", "You still have seven months to go.")
    PeopleSpeaking("      ", "It's a waste of resources to stay awake")
    PeopleSpeaking("      ", "You need to sleep until the space ship reaches mars.")
    answer = choiceInput("lying on the seat to sleep", "tie myself on the bulkhead")
    if(answer == 2):
        #good
        PeopleSpeaking("Clark","have a good dream")
    elif(answer == 1):
        #dead
        PeopleSpeaking("System alarm","mayday,mayday.It's Greenwich time two thirty-four")
        PeopleSpeaking("            "," alarm system, the ship was damaged,")
        PeopleSpeaking("            ","the failure of the mission console crash")
        print("")
        PeopleSpeaking("GAME TIP","Your body will float around in the space ship")
        PeopleSpeaking("        ","and damage the equipments if you don't tie yourself well")
        END()
        ForthOne()
    #leave some blank
    print("|")
    print("|")
    return
