while(True):
    a = input("Enter a number:")
    try:
        a = int(a)
        break
    except:
        print("that's not a number")
        continue
print(a)
