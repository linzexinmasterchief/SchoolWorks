#section created by Helen 3766 G2.Y on 3/11 To carry out an investigation on Mars
from lib import*
#----------------------------------1 choice---------------------------------
#Function to process question one
def onMars():
    SystemSpeaking("You have successfully landed on Hellas Planitia, Mars. Please wear suitable equipment and be ready for Mar’s atmosphere.")
    PeopleSpeaking("NASA","Composition Data: \n| Carbon dioxide 95.97% \n| Argon 1.93% \n| Nitrogen 1.89% \n| Oxygen 0.146% \n| Carbon monoxide 0.0557%. Do you want to wear your oxygen mask? ")
       
    answer = choiceInput("Yes", "No")
    if(answer == 2):
        SystemSpeaking("Danger！Mars' atmosphere is full of CO2 . You cannot breath.")
        END()
        onMars()
        
    elif(answer == 1):
        SecondOne()
    return

#----------------------------------2 choice---------------------------------
def SecondOne():   
    SystemSpeaking("Capsule gate opening…")
    PeopleSpeaking("NASA","Okay, please breathe normally as you did on earth. \n| You need to build a living hub for your accommodation and experiments. \n| You have two sites to choose from: site 1 is on a flat plain. site 2 is in a impact crater. ")
    PeopleSpeaking("NASA","Please remember, most of your equipment relies on solar energy. And, watch out for frequent sandstorms on Mars. Where do you want to build the hub? ")
    answer = choiceInput("site1","site2")
    
    if(answer == 2):
        PeopleSpeaking("Craters block a large proportion of sunlight. Cannot charge device sufficiently. Not enough energy for any system! Mission failed.")
        END()
        SecondOne()
        
    elif(answer == 1):
        ThirdOne()
    return


#----------------------------------3 choice---------------------------------
def ThirdOne():
    SystemSpeaking("Report Update: Congratulation, astronaut. All the devices are now full of charge and ready to work. \n| Be careful, a very strong sandstorm is moving towards you. Please stay inside the hub. ")
    PeopleSpeaking("NASA","storm info: scale:11 velocity: 70 MPH  distance: 15 Miles You are now collecting samples from Mars’atmosphere.15 minutes until collection complete. Do you want to wait until collection complete? "),
    answer = choiceInput("Yes", "No")
    if(answer == 1):
        ForthOne()
    elif(answer == 2):
        PeopleSpeaking("NASA","2 minutes until collection complete. But the sandstorm has arrived.")
        END()
        ThirdOne()    
    return

#----------------------------------4 choice---------------------------------
def ForthOne():
    SystemSpeaking("You have entered the hub. Congratulation, the sandstorm has passed, and the hub is intact.Do you want to check if all systems are still working properly?")
    answer = choiceInput("Yes","No")


    if(answer == 1):    
        FifthOne()
        
    elif(answer == 2):
        PeopleSpeaking("NASA","Report Update: Unknown error occurred at airlock 2. All food supply is stored nearby. An explosion has taken place.\nMission failed.\nAstronaut,always check the equipment.")
        END()
        ForthOne()
        
    return

#----------------------------------5 choice---------------------------------
def FifthOne():
    SystemSpeaking("Checking: central electricity… \n| air circulation… \n| water supply… \n| heating system…  F\n| ortunately, astronaut. All systems are working brilliantly. Next, Please pick up water ice samples from pole region. Rovers are ready.")
    PeopleSpeaking("NASA","\n| Geographical info: \n| current coordinates: 72°34’ E 55°63’ N water ice sample coordinates:  79°08’ E 69°21’ N")
    SystemSpeaking("Which way do you want to go?")
    answer = choiceInput("south west","north east")
   
    if(answer == 1):
        SystemSpeaking("You have driven 1080 km. The example taking spot should be only 530 km away.")
        PeopleSpeaking("NASA","Astronaut, are you sure you have taken the correct direction? There is not enough food supply for you to last for the return trip. \n| Mission failed")
        END()
        FifthOne()
                   
    elif(answer == 2):
        SixthOne()
        
    return

#----------------------------------6 choice---------------------------------
def SixthOne():
                    
    PeopleSpeaking("NASA","Very well, astronaut. You have arrived at the Planum Boreum. The spot foe sample collecting is only 1.2 km away.  Watch out, the land will be slippery from now on.")
    SystemSpeaking("Do you want to drive your rover nearer? ")
    answer = choiceInput("Yes","No")

    if(answer == 1):
        PeopleSpeaking("NASA","Too slippery!  The rover is stuck on this icy land. It cannot gain enough friction to plunge out. Mission failed.")
        END()
        SixthOne()

    elif(answer == 2):
        SeventhOne()

    return
        

    

#----------------------------------7 choice---------------------------------

def SeventhOne():

    PeopleSpeaking("NASA","You have successfully collected enough sample. But, the rover hasn't got sufficient power due to the extremely low temperature here. You can stay and wait for it to charge from the sunlight.")
    SystemSpeaking("Rover charging info: \n| 10% power: 1 h \n| 100% power: 10h \n| during charging, the rover cannot activate any system. \n| You cannot stop charging once charging mode is activated, until charging completes>> \n| current power: 2% \n| total power needed to return to the hub: 90%  \n\ temperature info: approx. -63°C \n| Spacesuit info: \n| current power: 76% \n| self-heating function hours left: 3h ")
    SystemSpeaking("How long do you want to charge your rover?")
    answer = choiceInput("3h","9h")

    if(answer == 2):
        PeopleSpeaking("NASA","It's been 3 hours. Spacesuit heating system run out of power. Rover heating system not available in charging mode. \n| The coldness has killed you. Remember, your safety is alway priority!")
        END()
        SeventhOne()

    elif(answer == 1):
        EighthOne()

    return
        
    
    

#----------------------------------8 choice---------------------------------

def EighthOne():
    PeopleSpeaking("NASA","Astronaut, though the rover is only 30% charged, we have to activate the system and turn on the heating. Or the coldness will kill you in this icy world. Please remember, your safety is the priority.")
    PeopleSpeaking("NASA","You have two course to choose: \n| 1.Planum Boreum-  Victoria crater - Mount Sharp - Hellas Planitia（Hub） total: 380km \n| 2.Planum Boreum- Acidalia Planitia - Isidis Planitia- Planum Angustum - Hellas Planitia（Hub） total: 660 km")
    PeopleSpeaking("DATABASE","planetary terms: \n| Crater=circular depression in the surface of a planet  \n| Planitia=plain  \n| Planum=plateau")
    SystemSpeaking("Which way do you want to choose?")
    answer = choiceInput("1","2")

    if (answer == 1):
        SystemSpeaking("You have driven into the crater, but cannot get out. The rover cannot provide enough traction to go up the steep slope.")
        PeopleSpeaking("NASA","You are trapped inside the crater. Remember always to avoid mountains and craters. They may be too steep for your rover.\n| Mission Failed")
        END()
        EighthOne()
    elif(answer == 2):
        NinthOne()    

    return

#----------------------------------9 choice---------------------------------

def NinthOne():
    PeopleSpeaking("NASA","This route is a good choice, astronaut. You can charge our rover on the way and save some energy too, since you are going on the plains.")
    PeopleSpeaking("NASA","Good, you have arrived at the hub. Congratulations, you have finished the mission. Now you have to plan going home.")
    SystemSpeaking("Report Update: Unknown error occurred to ascending shuttle( for return trip ). Engine failed. May be fuel leakage.")
    SystemSpeaking("Dangerous! What do you want to do?")
    answer = choiceInput("wait for instruction from NASA","examine it by yourself")

    if (answer == 2):
        print("| It is indeed fuel leakage…Please remember, stay away from any explosives. They may explode at any time.\n| Unfortunately, you are killed in this explosion.")
    elif(answer == 1):
        PeopleSpeaking("NASA","NASA Houston: Astronaut, there is an alternative way to go home. You can look for Schiaparelli lander. There may be components necessary for taking off from Mars.")

    return
    
    
    






