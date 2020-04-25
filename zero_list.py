import random
liste = []
history = []
lenhistory = []
counter = 0
high = 0

value = int(input('Enter a value : '))

for z in range(0,value):
    liste.append(random.randint(0,1))
print(liste)

if liste[0] == 0:
    history.append(0)
    lenhistory.append(0)
    
for a in range(0,len(liste)-1):
    if liste[a] == 0:
        lenhistory[-1] += 1

    elif liste[a] == 1 and liste[a+1] == 0:
        history.append(a + 1)
        lenhistory.append(0)

if liste[-1] == 0:
    lenhistory[-1] += 1

for b in range(0,len(lenhistory)):
    if lenhistory[b] > high:
        high = lenhistory[b]

for c in range(0,len(lenhistory)):
    if lenhistory[c] == high:
        break
    
print('history : ', history)
print('lenhistory : ', lenhistory)

if history != []:
    print('rank : ', history[c], ', length : ', high)
