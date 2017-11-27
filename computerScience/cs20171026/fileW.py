from lzxPyLib.StrongerInput import *

data = open("records.txt", "w")

amount = 0
while amount < 5:
	idStr = StringInput("Enter id: ")
	nameStr = StringInput("Enter name: ")
	classStr = StringInput("Enter class: ")

	if len(nameStr) >= 15:
		nameStr = nameStr[:15]
	else:
		for i in range(0, 15 - len(nameStr)):
			nameStr = nameStr + " "

	data.write(idStr + nameStr + classStr + "\n")

	amount += 1

data.close()
