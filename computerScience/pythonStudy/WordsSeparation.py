#initialize
#amount of higher case letters
HigherCase = 0
#amount of all letters
EveryAlphbet = 0
#output array(final answer)
output = []
#recieve input
Message = str(input('Please input a string : '))
#initialize the array for processing
Sentence = ['' for s in range(0,len(Message))]
#iterate every alphabet
while EveryAlphbet < len(Message):
    #the alphabet is capital or not
    if ord(Message[EveryAlphbet]) >= 65:
        if ord(Message[EveryAlphbet]) <= 90:
            #move to the next digit of Sentence
            #because a new capital letter is read
            HigherCase = HigherCase + 1
    #minus one because highercase added one first above
    Sentence[HigherCase - 1] = Sentence[HigherCase - 1] + Message[EveryAlphbet]
    #move to the next digit of Message
    #no matter it's capital or not
    EveryAlphbet = EveryAlphbet + 1
#clear all the useless blank spaces
#and transfer the processed sentence to the out put array
for word in Sentence:
    if word != '':
        output.append(word)
#print out the output
print(output)