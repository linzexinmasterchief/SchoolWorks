from lib import*
#chinese version
def CHmain():
    #start the game
    print("系统启动中...")
    print("系统正在上线...")
    print("| 位置: 地球")

    #system speaking
    SystemSpeaking("早上好, 舰长")

    #first choise in the game.
    t = choiceInput("怎么了?", "你好") 
    if(t == 1):
        secondOne()
    elif(t == 2):
        secondTwo()
    print("|")
    
    
def secondOne():
    PeopleSpeaking("地球", "你有了一个新任务,")
    print("|       我们需要你作为第一个登上火星的人类探索火星")
    
    
def secondTwo():
    PeopleSpeaking("地球", "你好,")
