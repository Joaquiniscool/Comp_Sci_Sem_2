x = int(input("how many numbers do you want"))
thislist = []
for i in range(0,x):
    import random
    y = random.randrange(0,10)
    
    thislist.append(y)
for i in range(0, x):
    print(thislist[i])
