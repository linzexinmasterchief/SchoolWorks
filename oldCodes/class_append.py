StudentName = []

StudentMark1 = []
StudentMark2 = []
StudentMark3 = []

classtotal1 = 0
classtotal2 = 0
classtotal3 = 0

classhigh1 = 0
classhigh2 = 0
classhigh3 = 0

classlow1 = 9999
classlow2 = 9999
classlow3 = 9999

for i in range(3):
    name = input("name:")
    StudentName.append(name)
    mark1 = input("mark1:")
    while True:        
        try:
            mark1 = float(mark1)
            if mark1 >= 0 and mark1 <= 20:
                break
            else:
                print("imposible!you are cheeting!!!")
                mark1 = input("mark1:")
        except:
            print("please enter number!")
            mark1 = input("mark1:")
    if mark1 > classhigh1:
        classhigh1 = mark1
    if mark1 < classlow1:
        classlow1 = mark1
    classtotal1 = classtotal1 + mark1
    StudentMark1.append(mark1)

    mark2 = input("mark2:")
    while True:        
        try:
            mark2 = float(mark2)
            if mark2 >= 0 and mark2 <= 30:
                break
            else:
                print("imposible!you are cheeting!!!")
                mark2 = input("mark2:")
        except:
            print("please enter number!")
            mark2 = input("mark2:")        
    if mark2 > classhigh2:
        classhigh2 = mark2
    if mark2 < classlow2:
        classlow2 = mark2
    classtotal2 = classtotal2 + mark2
    StudentMark2.append(mark2)

    mark3 = input("mark3:")
    while True:        
        try:
            mark3 = float(mark3)
            if mark3 >= 0 and mark3 <= 35:
                break
            else:
                print("imposible!you are cheeting!!!")
                mark3 = input("mark3:")
        except:
            print("please enter number!")
            mark3 = input("mark3:")
    if mark3 > classhigh3:
        classhigh3 = mark3
    if mark3 < classlow3:
        classlow3 = mark3
    classtotal3 = classtotal3 + mark3
    StudentMark3.append(mark3)
    
for i in range(3):
    print("name:",StudentName[i],"mark1:",StudentMark1[i],"mark2:",StudentMark2[i],"mark3:",StudentMark3[i])
    print("total is",StudentMark1[i]+StudentMark2[i]+StudentMark3[i])
print("T1:","Highest:",classhigh1,"Lowest:",classlow1,"Avg:",classtotal1)
print("T2:","Highest:",classhigh2,"Lowest:",classlow2,"Avg:",classtotal2)
print("T3:","Highest:",classhigh3,"Lowest:",classlow3,"Avg:",classtotal3)



