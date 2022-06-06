import datetime
people_list =[]
with open('People.txt') as f:
    for line in f:
        l = line.strip()
        print(l)

with open('Compliment.txt') as f:
    for line in f:
        l = line.strip()
        print(l)    
        people_list.apppend(l)
        
import random
numpeop = random.randrange(0, len(people_list)
numpeop = random.randrange(0, len(comp_list)

print(people_list[numpeop] + [num(comp)]

comp_list.apppend(l)
x = datetime.datetime.now()

print()
print("The date and time are:")
print(str(x.day) + "/" + str(x.month) + "/" + str(x.year) + " at " + str(x.hour))

f.close()
