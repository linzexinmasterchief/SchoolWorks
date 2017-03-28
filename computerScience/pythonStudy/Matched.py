def Matched(String1, String2):
    match = 0
    
    if len(String1) != len(String2):
        return 2
    for i in range (0, len(String1)):
        if ord(String1[i]) == ord(String2[i]):
            match = match + 1
        elif ord(String1[i]) == ord(String2[i]) + 32:
            match = match + 1
        elif ord(String2[i]) == ord(String1[i]) + 32:
            match = match + 1
    if match == len(String1):
        return 0
    if len(String1) - match == 1:
        return 1
    else:
        return 2

String1 = ""
out = False
while not out:
    out = False
    String1 = input("Enter the first string: ")
    if String1 == "":
        print("Wrong format!", end="")
        continue
    if String1[0] == " ":
        print("Wrong format!", end="")
        continue
    for i in range (0, len(String1)):
        if String1[i] == " ":
            out = True
            continue
        if String1[i].isalpha() == False:
            if ord(String1[i]) != 32:
                print("Wrong format!", end="")
                break
            else:
                out = True
        else:
            out = True

String2 = ""
out = False
while not out:
    out = False
    String2 = input("Enter the second string: ")
    if String2 == "":
        print("Wrong format!", end="")
        continue
    if String2[0] == " ":
        print("Wrong format!", end="")
        continue
    for i in range (0, len(String1)):
        if String2[i] == " ":
            out = True
            continue
        if String2[i].isalpha() == False:
            if ord(String2[i]) != 32:
                print("Wrong format!", end="")
                break
            else:
                out = True
        else:
            out = True
            
FuncOut = Matched(String1,String2)
print(FuncOut)
