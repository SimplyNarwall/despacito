"""
ID: kevinsh4
LANG: PYTHON3
TASK: milk
"""
#strawberry = open('milk.in')
#written = open('milk.out', 'w')
strawberry = open('C:/Users/kevin/OneDrive/Documents/SNAAAKES/noMoreUSACO/chocolate.txt') #really just chocolate.txt
written = open('C:/Users/kevin/OneDrive/Documents/SNAAAKES/noMoreUSACO/noonewantstodothis', 'w') #the file which i put the result
rawFarmerPrices = {}
for v, line in enumerate(strawberry): #processes all the really raw data
    if v == 0: 
        milkAmt = line.rstrip().split()[0]
    elif int(line.rstrip().split()[0]) in rawFarmerPrices:
        rawFarmerPrices[int(line.rstrip().split()[0])] += int(line.rstrip().split()[1])
    else:
        rawFarmerPrices[int(line.rstrip().split()[0])] = int(line.rstrip().split()[1])
whatUHave = 0
budget = 0

lol = list(rawFarmerPrices.keys()); lol.sort()
cheapPrices = {}
for key in lol: #sorts the dict from cheapest to expensive-est
    cheapPrices[key] = rawFarmerPrices[key]
print(len(rawFarmerPrices))

for price in cheapPrices: #the meat of the program
    if whatUHave + cheapPrices[price] >= int(milkAmt):
        for i in range(cheapPrices[price]):
            if whatUHave == int(milkAmt):
                from sys import exit
                written.write(str(budget) + '\n')
                exit(0)
            else:
                budget += price
                whatUHave += 1
    else:
        whatUHave += cheapPrices[price]
        budget += cheapPrices[price] * price
        print(whatUHave, budget)

#correct answer for the 7th run is 993159
written.write(str(budget) + '\n')
