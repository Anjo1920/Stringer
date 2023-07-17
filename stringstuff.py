# только комбаптильный с стрингом в переменне StringText
stringText = 'ad23f245323c'
stringList = []
watList = 0
num = 0
numMassive = 0

for i in range(0, 6):
    numWas = num
    num = num + 2 
    stringMassive = stringText[numWas:num]
    stringList.append('0x' + stringMassive)
    #stringList.append(stringMassive)
    
print(stringList)