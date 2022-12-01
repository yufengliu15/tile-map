# Full Name: Yufeng Liu
# Student #: 101258905

import random
random.seed()

fileName = input("Input a file name and extension to create: ")

while True:
    width = input("How big would you like the width to be? ")
    height = input("How big would you like the height to be? ")
    
    if width.isdigit() or height.isdigit():
        break
    else:
        print ("Improper input, try again. ")

fileHandle = open(fileName, "w")
tileMap = []

# puts the width and height at the top of the file, in the format: ('width', 'height')
fileHandle.write(f"{width, height} \n")

# we indent each list, to differentiate when to create a newline for the tiles
for y in range(int(height)):
    tempTileMap = []
    for x in range(int(width)):
        randomNum = random.randint(0,4)
        tempTileMap.append(randomNum)
    tileMap.append(tempTileMap)

# converts the 2d matrix into a '2d' string
tileMapString = ""
for i in range(int(height)):
    tempTileMapString = ""
    tempTileMapString = ','.join(map(str,tileMap[i]))
    tileMapString = tileMapString + tempTileMapString + "\n"

fileHandle.write(tileMapString)
fileHandle.close()