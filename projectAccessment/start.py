#Last modify 2016-10-29-23-23
#@Auther Blake
from Title import*
from EN import*
from LaunchRocket import*
from LifeInTheSpace import*
from LandingOnMars import*
from marrss import*
from Leaving import*

#chinese,still developing
from CH import*

#print title and all about the game, helps
printALL()

#save time
def startMission():
    ENmain()
    LaunchRocket()
    InSpace()
    MarsLanding()
    onMars()

#select which language does the player wants to use
print("choose your language请选择您的语言:")
language = choiceInput("English","中文")
if language == 1:
    startMission()
    print("EN finished")
elif language == 2:
    print("Still developing")
    print("jumping to Enlish virsion.")
    startMission()
    print("CH finished")
