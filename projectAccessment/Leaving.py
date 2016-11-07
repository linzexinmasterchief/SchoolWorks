#@Auther Blake

from lib import*

#----------------------------------1 choice---------------------------------
def LeftMars():
    PeopleSpeaking("Current Location","In the vehicle")
    PeopleSpeaking("System"," the temperature inside is too low for you")
    answer = choiceInput("Turn on the heater inside the vehicle\n","try to find something else to use as a heater")
    if(answer == 1):
        LeftMars()
    elif(answer == 2):
        SecondOne()
    return
