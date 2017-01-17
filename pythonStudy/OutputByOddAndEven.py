Times = input()
try:
    Times = int(Times)
except:
    print()
for j in range (0,Times):
    In = input()
    if In == "":
        break
    Out = []

    for i in range (0,len(In)):
        if i % 2 == 0:
            Out.append(In[i])
    Out.append(" ")
    for i in range (0,len(In)):
        if i % 2 == 1:
            Out.append(In[i])
    a = ""
    for i in range (0,len(Out)):
        print(Out[i],end="")
    print()
