print("lzx")
a=[1234]
while True:
    password = 0
    try:
        password = int(input("enter password"))
    except:
        pass
    if password == a[0]:
        ans = input("do you want to change password?")
        if ans == "yes":
            a[:] = [input("password:")]
        else:
            print("haha")
    else:
        print("hehe")