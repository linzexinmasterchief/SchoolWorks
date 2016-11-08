#section created by Michael 3778 G2.Y on 8/11 To carry out the introduction of the mission
#Last modify 2016-10-29-23-23

from lib import*


#----------------------------------1 choice---------------------------------
#first function used in the english program
def ENmain():
    #initialize score
    #start the game
    print("System starting...")
    print("Bringing the system online...")
    PeopleSpeaking("Location","Earth")

    #system speaking
    SystemSpeaking("Good morning, captain.")

    #first choise in the game
    answer = choiceInput("what happened?", "Hi") 
    if(answer == 1):
        #ask if the player wants the misson
        secondOne()
    elif(answer == 2):
        #say "HI" to the player
        secondTwo()
    print("|")
    return

#----------------------------------2 choice---------------------------------
#launch if player say "what happened?"
def secondOne():
    PeopleSpeaking("Earth","You've recieved a mission,")
    print("|         we need you to be the first person to explore the mars.")
    answer = choiceInput("negative","affirmative") 
    if(answer == 2):
        #send the mission
        ThirdOne()
    elif(answer == 1):
        #Try to make the player to start the mission
        ThirdTwo()
    return

#launch if player say "Hi"    
def secondTwo():
    PeopleSpeaking("Earth", "Hi,captain.")
    answer = choiceInput("anything need me to do?", "...")
    if(answer == 1):
        #send the mission
        ThirdOne()
    elif(answer == 2):
        #answer again :)
        secondTwo()
    return

#----------------------------------3 choice---------------------------------
#launch if player say "affirmative"/"anything need me to do?"
def ThirdOne():
    PeopleSpeaking("Earth", "wait a minute,I will send the message to your system.")
    answer = choiceInput("stop", "continue") 
    if(answer == 2):
        #continue to send the message
        ForthOne()
    elif(answer == 1):
        #jump to the negative/stop
        ThirdTwo()
    return

#launch if player say "negative"/"stop"
def ThirdTwo():
    PeopleSpeaking("Earth", "are you sure about this?")
    #a special END function in module lib.py
    END()
    #send the player back to mission
    #player will quit the game in the END() function if they really want to do that
    secondOne()
    return

#----------------------------------4 choice---------------------------------
#launch if player say "continue"
def ForthOne():
    PeopleSpeaking("System", "new message.")
    answer = choiceInput("open it", "read the title") 
    if(answer == 1):
        #open the message
        fifthOne()
    elif(answer == 2):
        #print the brief message
        fifthTwo()
    return

#----------------------------------5 choice---------------------------------
#launch if the player say "open it"
def fifthOne():
    PeopleSpeaking("message", "human beings can already land on moon now.")
    print("           We should explore further to mars and the solar system.")
    print("           You may decide how to make your space ship in the develop lab")
    print("           May luck and our wish be with you")
    PeopleSpeaking("System","--message ends--")
    answer = choiceInput("...","go to develop lab")
    if(answer == 2):
        #Next level
        Next()
    elif(answer == 1):
        #Next level
        Next()
    return

#launch if the player say "read the title"
def fifthTwo():
    PeopleSpeaking("message", "go to develop lab")
    answer = choiceInput("open message", "go to develop lab")
    if(answer == 1):
        #open the message
        fifthOne()
    elif(answer == 2):
        #Next level
        Next()
    return

#----------------------------------6 choice---------------------------------
#jump to next file
def Next():
    #leave some blank
    print("|")
    print("|")
    return
