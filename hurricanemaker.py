import random
north = random.randint(0, 42)
west = random.randint(6, 97)
length = random.randint(10, 15)
firstintensity = random.randint(30, 40)
print(str(north)+" "+str(west) + " " + str(firstintensity))
halfdone = length/2
halfdone2 = 0
for i in range(0, length):
    print(halfdone2)
    print(halfdone)
    
    addnorth = str(random.randint(1, 2))
    addwest = str(random.randint(2, 3))
    addstrength = str(random.randint(5, 20))
    minusstrength = str(random.randint(5,10))
    firstintensity += random.randint(1,5)
    if random.randint(0, 1) == 1:
            pass
    else:
        addnorth = str(int(int(addnorth) - (int(addnorth) * 2)))
    if random.randint(0, 1) == 1:
        pass
    else:
        addwest = str(int(int(addwest) - (int(addwest) * 2)))
    if halfdone2 < halfdone:
        if random.randint(0, 1) == 1:
            pass
        else:
            addstrength = str(int(int(minusstrength) - (int(minusstrength) * 2)))
    elif halfdone2 >= halfdone:
        addstrength = -(int(addstrength) - random.randint(5,10))
        #addstrength = str(-int(int(minusstrength) - (int(minusstrength) * 2)))
    print(str(int(north) + int(addnorth)) + " " + str(int(west) + int(addwest)) + " " + str(int(firstintensity) + int(addstrength)))
    north += int(addnorth)
    west += int(addwest)
    firstintensity += int(addstrength)
    halfdone2 += 1
