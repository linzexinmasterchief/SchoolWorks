from lzxPyLib.StrongerInput import *

target = StringInput("Enter the number you want to search: ")
targetFound = False

records = []
data = open("records.txt", "r")
while True:
    line = data.readline()
    if not line:
        break
    records.append(line)

for item in records:
	if target == item[:4]:
		print(item)
		targetFound = True
		break

if not targetFound:
	print("id not found")

data.close()