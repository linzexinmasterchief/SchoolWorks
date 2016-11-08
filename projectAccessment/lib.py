#Last modify 2016-10-30-11-53
#@Auther Michael 3778
#@version 1.7
from Title import*

# check if input type equals to TYPE
#function used:type()

def checkType(INPUT, TYPE):
    try:
        INPUT = type(TYPE)(INPUT)
        return True
    except:
        return False

# no error in this part 2016-10-30-12-01 by @Michael 3778


# check if enter is number(integer)
#function used:input(),checkType(),SystemSpeaking()

def NumInput(context):
    while True:
        enter = input(context)
        if (enter == "exit"):
            exit(0)
        if (enter == "help"):
            printHelp()
            continue
        if (checkType(enter, 0)):
            enter = int(enter)
            return enter
        SystemSpeaking("Invalid!")
        continue

# no error in this part 2016-10-30-12-01 by @Michael 3778


# check if enter is string
#function used:input(),checkType(),SystemSpeaking()

def TextInput(context):
    while True:
        enter = input(context)
        if (enter == "exit"):
            exit(0)
        if (enter == "help"):
            printHelp()
            continue
        if (checkType(enter, " ")):
            enter = str(enter)
            return enter
            SystemSpeaking("Invalid!")
        continue

# no error in this part 2016-10-30-12-01 by @Michael 3778


# check the enter range range1<=Input<=range2
#function used:NumInput(),SystemSpeaking()

def RangeNumberInput(context, range1, range2):
    while True:
        enter = NumInput(context)
        if (enter >= range1):
            if (enter <= range2):
                return enter
            else:
                SystemSpeaking("out of bound")
                continue
        else:
            SystemSpeaking("out of bound")
            continue

# no error in this part 2016-10-30-12-01 by @Michael 3778


# make choices
#function used:checkType(),RangeNumberInput()

def choiceInput(c1,c2):
	if checkType(c1,""):
		if checkType(c2,""):
			context = "|    1."+c1+"  2."+c2+"\n| >"
			choice = RangeNumberInput(context,1,2)
			return choice

# no error in this part 2016-10-30-12-01 by @Michael 3778


# different people talking
#function used:print()

def SystemSpeaking(text):
    print("| system  [",text,"]\n| ")

def PeopleSpeaking(name,text):
    print("|",name,":",text,"\n| ")

def PlayerSpeaking():
    return print("| > \n| "),

# no error in this part 2016-10-30-12-01 by @Michael 3778

#mission ends

def END():
    print("-------MISSION FAILED!--------")
    print("Do you want to stop your journy?")
    answer = choiceInput("Yes!stop!", "ah...wait a second...")
    if(answer == 1):
        print("--your story is finished,but,is there any better choices?--")
        #-----_
        exit(0)#--only for now
        #_____-
    elif(answer == 2):
        return
