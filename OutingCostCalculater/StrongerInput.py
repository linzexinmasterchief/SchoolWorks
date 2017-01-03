#Last modify 2016-10-30-11-53
#@Auther Michael 3778
#@version 1.7

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
            continue
        if (checkType(enter, 0)):
            enter = int(enter)
            return enter
        print("Invalid!")
        continue

# no error in this part 2016-10-30-12-01 by @Michael 3778


# check if enter is string
#function used:input(),checkType(),SystemSpeaking()

def TextInput(context):
    while True:
        enter = input(context)
        if (enter == "exit"):
            exit(0)
        if (checkType(enter, " ")):
            enter = str(enter)
            return enter
            print("Invalid!")
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
                print("out of bound")
                continue
        else:
            print("out of bound")
            continue

# no error in this part 2016-10-30-12-01 by @Michael 3778