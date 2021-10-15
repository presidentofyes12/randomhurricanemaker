import random
north = random.randint(0, 42)
west = random.randint(6, 97)
#length = random.randint(10, 15)
length = 8
firstintensity = random.randint(30, 40)
print(str(north)+" "+str(west) + " " + str(firstintensity))
halfdone = length/2
halfdone2 = 0
for i in range(0, length):
    """print("Halfdone2: " + str(halfdone2))
    print("Halfdone: " + str(halfdone))"""
    
    addnorth = str(random.randint(1, 2))
    addwest = str(random.randint(2, 3))
    addstrength = str(random.randint(5, 20))
    minusstrength = str(random.randint(5,10))
    firstintensity += random.randint(1,5)
    if random.randint(0, 1) == 1:
            pass
    else:
        addnorth = str(int(int(addnorth) - (int(addnorth) * 1.25)))
    if random.randint(0, 1) == 1:
        pass
    else:
        addwest = str(int(int(addwest) - (int(addwest) * 1.25)))
    if halfdone2 < halfdone:
        if random.randint(0, 1) == 1:
            print(str(int(north) + int(addnorth)) + " " + str(int(west) + int(addwest)) + " " + str(int(firstintensity) + int(addstrength)))
            firstintensity += int(addstrength)
        else:
            print(str(int(north) + int(addnorth)) + " " + str(int(west) + int(addwest)) + " " + str(int(firstintensity) - int(addstrength)))
            firstintensity -= int(addstrength)
    elif halfdone2 >= round(halfdone):
        print(str(int(north) + int(addnorth)) + " " + str(int(west) + int(addwest)) + " " + str(int(firstintensity) - int(addstrength)))
        firstintensity -= int(addstrength)
    north += int(addnorth)
    west += int(addwest)
    halfdone2 += 1
