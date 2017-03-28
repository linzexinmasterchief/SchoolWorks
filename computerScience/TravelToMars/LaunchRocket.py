#section created by Johnson G2.Y To carry out the preparation before launch
#Last modify 2016-10-29-23-23

from lib import*

#rockets number
rocket = 0
#fuel choosed
fuel = 0
#database
resource = [fuel,rocket]
#print the resouce you used
#def printResource():
#    for i in resource:
#        print i

#----------------------------------1 choice---------------------------------
#launch first
def LaunchRocket():
    PeopleSpeaking("System", "Entering the lab...")
    PeopleSpeaking("Scientist","welecom,captain.We are going to help you to build your spaceship")
    answer = choiceInput("How?", "Thanks")
    if(answer == 1):
        #Explain a little
        PeopleSpeaking("Scientist","You are going to plan how much rocket you will launch on your rocket")
        print("|        Think about the planet you are going and how much fuel do you want to")
        print("|        bring.Are you ready?Let's start.")
        SecondOne()
    elif(answer == 2):
        #directly start
        SecondOne()
    return

#----------------------------------2 choice---------------------------------
#launch if player say "How?"/"Thanks"
def SecondOne():
    PeopleSpeaking("Scientist","Which planet will you choose to go to?")
    answer = choiceInput("Jupiter","Mars")
    if(answer == 2):
        #good choice
        PeopleSpeaking("Scientist","That's fine")
        ThirdOne()
    elif(answer == 1):
        #sorry,choose again :)
        PeopleSpeaking("Scientist","Ah...I don't think landing on a gaseous planet is a good choice.")
        PeopleSpeaking("         ","Also,you should focus on your mission,don't be childish.")
        SecondOne()
    return

#----------------------------------3 choice---------------------------------
#launch if player say "mars"
def ThirdOne():
    PeopleSpeaking("Scientist","well,you may want to select some friends to go with you.")
    print("| You want to bring:"),
    answer = choiceInput("less or equals 7 and more than or equals 1", "more than 7")
    if(answer == 1):
        #good choice
        PeopleSpeaking("Scientist","Pass,enjoy your trip.")
        ForthOne()
    elif(answer == 2):
        #sorry,choose again :)
        PeopleSpeaking("Scientist","well,the most up-to-date space shuttle could only hold 7 astronauts")
        PeopleSpeaking("         ","I'm sorry but you need to leave someone on earth")
        ThirdOne()
    return

#----------------------------------4 choice---------------------------------
#launch if player say "<= 7 and >= 1"
def ForthOne():
    PeopleSpeaking("Scientist","The space shuttle is ready.But it needs some small rockets act as")
    print("|        the propeller,you want to install how many rockets?")
    print("| number of the small rockets You want to bring:"),
    answer = choiceInput("only one","two or more")
    if(answer == 2):
        #good choice
        PeopleSpeaking("Scientist","good choice")
        #record how many rocket did the player bring
        rocket = 3
        FifthOne(rocket)
    elif(answer == 1):
        #sorry,choose again :)
        PeopleSpeaking("Scientist","ok")
        #record how many rocket did the player bring
        rocket = 1
        FifthOne(rocket)
    return

#----------------------------------5 choice---------------------------------
#launch if player say "<= 4 and >= 2"
def FifthOne(rocket):
    PeopleSpeaking("Scientist","The propellers are installed, you need to fill them up with fuel")
    print("| You want to use:"),
    answer = choiceInput("Liquid hydrogen", "gasoline")
    if(answer == 1):
        if(rocket == 3):
            #good choice
            PeopleSpeaking("Scientist","ah,you are good at this,aren't you?")
            #record which type of fuel does the player add
            fuel = 1
            SixthOne(rocket,fuel)
        elif(rocket == 1):
            #good choice
            PeopleSpeaking("Scientist","I think this will be a moon spaceship...")
            #record which type of fuel does the player add
            fuel = 1
            SixthOne(rocket,fuel)
    elif(answer == 2):
        #sorry,choose again :)
        PeopleSpeaking("Scientist","fine,I'm glad I won't need to go with you")
        #record which type of fuel does the player add
        fuel = 2
        SixthOne(rocket,fuel)
    return

#----------------------------------6 choice---------------------------------
#launch
def SixthOne(rocket,fuel):
    PeopleSpeaking("Scientist","Ok,let's make a little test for your rocket")
    print("|    5-4-3-2-1-launch!")
    if(fuel == 2):
        PeopleSpeaking("Scientist","Whohhhhhh,that is a nice firework,but it won't be fun")
        PeopleSpeaking("         ","if you are in it.You need to redesign your fuel!")
        print("| >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> |")
        ForthOne()
    if(rocket == 1):
        PeopleSpeaking("Scientist","I,m sorry,captain.But your rocket can only go to moon.")
        PeopleSpeaking("         ","You may want to redesign your small rocket.")
        print("| >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> |")
        ForthOne()
    if(rocket == 3 & fuel == 1):
        print("| >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> |")
        PeopleSpeaking("Scientist","nice job,captain!Now you may start your trip.")
        print("|")
        print("|")
        return

   #leave some blank
    print("|")
    print("|")
    return
