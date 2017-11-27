from lzxPyLib.StrongerInput import *

target = StringInput("Enter the number you want to search: ")
targetFound = False

records = []
data = open("records.txt", "r+")
while True:
    line = data.readline()
    if not line:
        break
    records.append(line)

count = 0
for item in records:
	if target == item[:4]:
		nameStr = StringInput("Enter new name: ")

		if len(nameStr) >= 15:
			nameStr = nameStr[:15]
		else:
			for i in range(0, 15 - len(nameStr)):
				nameStr = nameStr + " "
		targetFound = True
		break
	count += 0
records[count] = item[:4] + nameStr + item[19:]

data.close()
data = open("records.txt", 'w')

if not targetFound:
	print("id not found")
else:
	for item in records:
		data.write(item)

data.close()