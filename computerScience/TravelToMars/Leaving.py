#section created by Blake G2.Y To carry out the leaving process
#@Auther Blake

from lib import*

name = " "

#----------------------------------1 choice---------------------------------
def LeftMars():
    print("After a long way on mars...")
    print("| you finally reached the location of the space ship, but...")
    PeopleSpeaking(">","oh my god...The spaceship is already damaged,I can't use it.")
    answer = choiceInput("try to connect with earth\n| ","drive the vehicle to try to find something")
    if(answer == 1):
        SystemSpeaking("you used up the fuel very soon and find nothing")
        END()
        LeftMars()
    elif(answer == 2):
        SecondOne()
    return

#----------------------------------2 choice---------------------------------
def SecondOne():
    PeopleSpeaking("System","there was a spaceship arriving on Mars in 1996,\n | its location is （45’51’’，75’84’’）")
    answer = choiceInput("Turn on the heater inside the vehicle\n| ","try to find something else to use as a heater")
    if(answer == 1):
        SystemSpeaking("The heater costs too much fuel, the vehicle didn’t go too far")
        END()
        SecondOne()
    elif(answer == 2):
        ThirdOne()
    return

#----------------------------------3 choice---------------------------------
def ThirdOne():
    PeopleSpeaking("System","you get into the ship")
    answer = choiceInput(" Use radioactive cells\n| ","use normal cells")
    if(answer == 2):
        SystemSpeaking("the energy has been used up quite soon!")
        END()
        ThirdOne()
    elif(answer == 1):
        SystemSpeaking("The heating effects are very good")
        ForthOne()
    return

#----------------------------------4 choice---------------------------------
def ForthOne():
    PeopleSpeaking("System","The temperature inside the vehicle is now stable")
    answer = choiceInput("take off the suit, easier to move around\n| ","keep the suit on")
    if(answer == 1):
        SystemSpeaking("the radioactive matters are toxic!")
        END()
        ForthOne()
    elif(answer == 2):
        SystemSpeaking("keep on looking for the spaceship")
        FifthOne()
    return

#----------------------------------5 choice---------------------------------
def FifthOne():
    PeopleSpeaking("| >","Ah, I find the ship!")
    PeopleSpeaking("System","the fuel left might not be enough for the trip back to earth")
    answer = choiceInput("Try to connect with the earth\n| ","Turn it on and have a try")
    if(answer == 2):
        SystemSpeaking("the fuel costs quicker than you think!")
        END()
        FifthOne()
    elif(answer == 1):
        PeopleSpeaking("Commander","I’ll send a ship to Mars, but it'll takes 6 months")
        SixthOne()
    return

#----------------------------------6 choice---------------------------------
def SixthOne():
    PeopleSpeaking("System","You would need enough food during 6 months, food left in the ship is\n| not much, you decide to farm by yourself, you would choose")
    answer = choiceInput("Potato\n| ","wheat")
    if(answer == 2):
        SystemSpeaking("soil on Mars doesn’t contain some elements for wheat growing!")
        END()
        SixthOne()
    elif(answer == 1):
        PeopleSpeaking("System","soil on Mars is good for potatoes growing")
        SeventhOne()
    return

#----------------------------------7 choice---------------------------------
def SeventhOne():
    PeopleSpeaking("System","Growing of potatoes needs Nitrogen, you would get Nitrogen from")
    answer = choiceInput("faeces\n| ","decompose hydrazine")
    if(answer == 2):
        SystemSpeaking("dangerous and explosive!")
        END()
        SeventhOne()
    elif(answer == 1):
        PeopleSpeaking("System","Safe and easy to get")
        EighthOne()
    return

#----------------------------------8 choice---------------------------------
def EighthOne():
    PeopleSpeaking("System","While the ship arrive at Mars, to save time and fuel\n| the ship doesn’t plan to land, you drive your ship next to the ship, you would")
    answer = choiceInput("manual operation butt joint\n| ","abandon your ship and get into the other ship")
    if(answer == 1):
        SystemSpeaking("manual operation is very dangerous!")
        END()
        EighthOne()
    elif(answer == 2):
        PeopleSpeaking("System","get into the ship safely")
        Next()
    return

#------------------------------------next-----------------------------------
def Next():
    print("| You've completed your mission and survived from all the dangers!")
    print("| Leave your name and let people remember you!")
    #use global variable to pass the value
    name = TextInput("| your name: ")
    Prize(name)

#-----------------------------------Prize-----------------------------------
def Prize(name):
    print("     +------------+")
    print("    /              \\")
    print("   /   ",name,"   \\")
    print("   |                 |")
    print("   | the first human |")
    print("   |                 |")
    print("   |    on mars!     |")
    print("   |                 |")
    print("   \\                /")
    print("    +---------------+")
    print("    /  /  /  /\\  \\  \\  \\")
    print("   /  /  /  /  \\  \\  \\  \\")
    print("  +--+--+--+    +--+--+--+")
