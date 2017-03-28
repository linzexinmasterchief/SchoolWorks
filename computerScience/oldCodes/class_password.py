for a in range(1,4):
    x = 0
    try:
        x = input("enter password:")
    except:
        pass
    if x == "123":
        print("log-in successfully")
        break
    else:
        print("log-in failed,please re-input your password")
        c += 1
if c >= 3:
    print("You have exceeded the number of tries.Please contact your administrator")
