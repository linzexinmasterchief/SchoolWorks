a = input("enter something:")
b = 0
try:
    a = int(a)
    b = 0
except:
    try:
        a = str(a)
        b = 1
    except:
        b = 2
if b == 0:
    print("you entered a number")
elif b == 1:
    print("you entered a string")
else:
    print("you didn't enter either number or string")
