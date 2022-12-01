# Full Name: Yufeng Liu
# Student #: 101258905

import pygame

# -----------------------------------------------------------------------------------------
# goes to the folder to look for the gifs
desertTile0 = pygame.image.load("Tile Images for Tutorial 08/tutorial_file_desert_0.gif")
desertTile1 = pygame.image.load("Tile Images for Tutorial 08/tutorial_file_desert_1.gif")
desertTile2 = pygame.image.load("Tile Images for Tutorial 08/tutorial_file_desert_2.gif")
desertTile3 = pygame.image.load("Tile Images for Tutorial 08/tutorial_file_desert_3.gif")
desertTile4 = pygame.image.load("Tile Images for Tutorial 08/tutorial_file_desert_4.gif")

forestTile0 = pygame.image.load("Tile Images for Tutorial 08/tutorial_file_forest_0.gif")
forestTile1 = pygame.image.load("Tile Images for Tutorial 08/tutorial_file_forest_1.gif")
forestTile2 = pygame.image.load("Tile Images for Tutorial 08/tutorial_file_forest_2.gif")
forestTile3 = pygame.image.load("Tile Images for Tutorial 08/tutorial_file_forest_3.gif")
forestTile4 = pygame.image.load("Tile Images for Tutorial 08/tutorial_file_forest_4.gif")

# -----------------------------------------------------------------------------------------
# user input, checks for files
while True:
    fileName = input("Input a file name to read from: ")
    try:
        fileHandle = open(fileName, "r")
    except:
        print ("The file doesn't exist, try again")
    else:
        break

while True:
    typeOfTiles = input("Which tile map would you like to use? desert('d') or forest('f'): ").lower()
    if typeOfTiles == 'f' or typeOfTiles == 'd':
        break
    else:
        print ("Not an option, try again.")

# -----------------------------------------------------------------------------------------
# finds the width and height from the top of the file
widthIndexStart = fileHandle.readline().find("'")
# readline continues to the next line, .seek() makes it go back to the start
fileHandle.seek(0,0)
widthIndexEnd = fileHandle.readline().find("'", widthIndexStart + 1)
fileHandle.seek(0,0)
width = int(fileHandle.readline()[widthIndexStart + 1:widthIndexEnd])
fileHandle.seek(0,0)

heightIndexStart = fileHandle.readline().find("'", widthIndexEnd + 1)
fileHandle.seek(0,0)
heightIndexEnd = fileHandle.readline().find("'", heightIndexStart + 1)
fileHandle.seek(0,0)
height = int(fileHandle.readline()[heightIndexStart + 1:heightIndexEnd])

# -----------------------------------------------------------------------------------------
# sets up displays
screen = pygame.display.set_mode((width*64,height*64))
background = pygame.Surface((width*64,height*64))
counterX = 0
counterY = 0

# -----------------------------------------------------------------------------------------
# finding and determining tile type and placement
for y in fileHandle:
    for character in y:
        if character == "0":
            if typeOfTiles == 'f':
                screen.blit(forestTile0,(counterX * 64, counterY*64))
            else:
                screen.blit(desertTile0,(counterX * 64, counterY*64))
        elif character == "1":
            if typeOfTiles == 'f':
                screen.blit(forestTile1,(counterX * 64, counterY*64))
            else:
                screen.blit(desertTile1,(counterX * 64, counterY*64))
        elif character == "2":
            if typeOfTiles == 'f':
                screen.blit(forestTile2,(counterX * 64, counterY*64))
            else:
                screen.blit(desertTile2,(counterX * 64, counterY*64))
        elif character == "3":
            if typeOfTiles == 'f':
                screen.blit(forestTile3,(counterX * 64, counterY*64))
            else:
                screen.blit(desertTile3,(counterX * 64, counterY*64))
        elif character == "4":
            if typeOfTiles == 'f':
                screen.blit(forestTile4,(counterX * 64, counterY*64))
            else:
                screen.blit(desertTile4,(counterX * 64, counterY*64))
        else: 
            continue
        counterX += 1
    counterY += 1
    counterX = 0
    
pygame.display.update()
pygame.time.delay(2000)
pygame.image.save(screen, "tile_map.png")

fileHandle.close()