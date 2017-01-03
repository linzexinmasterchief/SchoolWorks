#Last modify 2017-1-3-20-46
#@Auther Michael 3778
#@version 1.0

from StrongerInput import*
"""
introduction:
    this program can give you a list of peoples name and identifi whether
    it will make profit or not, to make sure the program works properly, 
    you should follow the guide lines below.
program user guide:
    1.the number of citizens should be larger than 10 and smaller than 36
    2.example of entering name and money:

        Enter citizen's name:f4
        Enter the amount of money this person paid:f3
        Invalid!
        Enter the amount of money this person paid:f
        Invalid!
        Enter the amount of money this person paid:f4f
        Invalid!
        Enter the amount of money this person paid:2

        you can enter what ever you want as name
        but the money should be larger than 0 and smaller than 100000000

Have fun with the program!
"""
#an array with information from TaskOne in it
DataOne   = []
#total money
DataTwo   = 0.00
#show if the program finished successfully or not
DataThree = 0
"""work out user's input"""
def TaskOne():
    #initialize variables for "Amount"
    CitizenAmount = 0
    CarerAmount   = 0
    TotalAmount   = 0
    #initialize variables for "cost"
    CoachCost     = 0
    MealCost      = 0.00
    TicketCost    = 0.00
    TotalCost     = 0.00
    PersonCost    = 0.00
    #asign the total amount of Citizen,excluding carers
    CitizenAmount = RangeNumberInput("Please Enter the number of the citizens:", 10, 36)
    #first assume there are two carers
    CarerAmount = 2
    #if the amount of citizen is larger than 24, change the amount of carer to 3
    if(CitizenAmount > 24):
        CarerAmount = CarerAmount + 1
    #calculate the TotalAmount of people
    TotalAmount = CitizenAmount + CarerAmount
    #identify which situation it is and assign the "cost" values
    if(12 <= TotalAmount <= 16):
        CoachCost  = 150
        MealCost   = 14.00 * CitizenAmount
        TicketCost = 21.00 * CitizenAmount
    elif(17 <= TotalAmount <= 26):
        CoachCost  = 190
        MealCost   = 13.50 * CitizenAmount
        TicketCost = 20.00 * CitizenAmount
    elif(27 <= TotalAmount <= 39):
        CoachCost  = 225
        MealCost   = 13.00 * CitizenAmount
        TicketCost = 19.00 * CitizenAmount
    else:
        #do nothing
        pass
    #the amount of money needs in total
    TotalCost  = CoachCost + MealCost + TicketCost
    #the amount of money each citizen costs
    PersonCost = TotalCost / CitizenAmount
    #datas that are important for later calculations/need to be return
    ReturnData = [TotalCost, PersonCost, CitizenAmount, CarerAmount]
    #return the finall values to the main program by a list
    return ReturnData
"""print the name list and calculate the total money"""
def TaskTwo(DataOne):
    #initialize the array and variable(DataOne[2] + DataOne[3] = the total amount of people)
    NameList   = ["" for i in range (0, DataOne[2] + DataOne[3])]
    MoneyList  = [0 for i in range (0, DataOne[2] + DataOne[3])]
    TotalMoney = 0.00
    #get everybody's name from the input(DataOne[3] is the amount of carers)
    for i in range (0, len(NameList)):
        print("\npeople",i + 1,":")
        if(i < DataOne[3]):
             NameList[i]  = TextInput("Enter carer's name:")
        else:
            NameList[i]  = TextInput("Enter citizen's name:")
        MoneyList[i] = RangeNumberInput("Enter the amount of money this person paid:",0,100000000)
    #asign 0 to carer's money because they don't need to pay(DataOne[3] is the amount of carers)
    for i in range (0, DataOne[3]):
        MoneyList[i] = 0
    #iterate NameList to print the namelist
    print("\n-------------------------------")
    print("   identity     name           ")
    print("-------------------------------")
    for i in range (0, len(NameList)):
    #first print carers, then citizens(DataOne[3] is the amount of carers)
        if(i < DataOne[3]):
            print("   Carer        ", NameList[i])
        else:
            print("   citizen      ", NameList[i])
    print("-------------------------------")
    #iterate MoneyList to get TotalMoney
    for i in MoneyList:
        TotalMoney = TotalMoney + i
    #return the TotalMoney to the main program by a value
    return TotalMoney
"""identify if the outing made profit or not"""
def TaskThree(DataOne,DataTwo):
    if(DataOne[0] > DataTwo):
        print("the outing has broken with a \"profit\" of", DataTwo - DataOne[0])
    elif (DataOne[0] < DataTwo):
        print("the outing has made a profit of", DataTwo - DataOne[0])
    else:
        print("the profit is zero but didn't break")
    #normal = 0, not good = other values
    return 0
"""main program"""
DataOne = TaskOne()
print(DataOne[0])
DataTwo = TaskTwo(DataOne)
DataThree = TaskThree(DataOne,DataTwo)