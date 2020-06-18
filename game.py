import random

import pygame

pygame.init()

size = screenWidth, screenHeight = 648, 720

#set size of the window
screen = pygame.display.set_mode(size)

# just the background image
background = pygame.image.load('tiles/background.png')
# where the objects hide the character
foreground = pygame.image.load('tiles/foreground.png')

# set title of the window
pygame.display.set_caption("Data Mining Game")

# helps determine the FPS
clock = pygame.time.Clock()

#load then play music
music = pygame.mixer.music.load("bgm.wav")
pygame.mixer.music.play()

# loading characters sprites
# character_1
character_1_walkup = [pygame.image.load('./sprites/character_1/U1.png'),
                      pygame.image.load('./sprites/character_1/U2.png'),
                      pygame.image.load('./sprites/character_1/U3.png'),
                      pygame.image.load('./sprites/character_1/U4.png')]
character_1_walkdown = [pygame.image.load('./sprites/character_1/D1.png'),
                        pygame.image.load('./sprites/character_1/D2.png'),
                        pygame.image.load('./sprites/character_1/D3.png'),
                        pygame.image.load('./sprites/character_1/D4.png')]
character_1_walkright = [pygame.image.load('./sprites/character_1/R1.png'),
                         pygame.image.load('./sprites/character_1/R2.png'),
                         pygame.image.load('./sprites/character_1/R3.png'),
                         pygame.image.load('./sprites/character_1/R4.png')]
character_1_walkleft = [pygame.image.load('./sprites/character_1/L1.png'),
                        pygame.image.load('./sprites/character_1/L2.png'),
                        pygame.image.load('./sprites/character_1/L3.png'),
                        pygame.image.load('./sprites/character_1/L4.png')]
#character_2
character_2_walkup = [pygame.image.load('./sprites/character_2/U2.png'),
                      pygame.image.load('./sprites/character_2/U2.png'),
                      pygame.image.load('./sprites/character_2/U3.png'),
                      pygame.image.load('./sprites/character_2/U4.png')]
character_2_walkdown = [pygame.image.load('./sprites/character_2/D2.png'),
                        pygame.image.load('./sprites/character_2/D2.png'),
                        pygame.image.load('./sprites/character_2/D3.png'),
                        pygame.image.load('./sprites/character_2/D4.png')]
character_2_walkright = [pygame.image.load('./sprites/character_2/R2.png'),
                         pygame.image.load('./sprites/character_2/R2.png'),
                         pygame.image.load('./sprites/character_2/R3.png'),
                         pygame.image.load('./sprites/character_2/R4.png')]
character_2_walkleft = [pygame.image.load('./sprites/character_2/L2.png'),
                        pygame.image.load('./sprites/character_2/L2.png'),
                        pygame.image.load('./sprites/character_2/L3.png'),
                        pygame.image.load('./sprites/character_2/L4.png')]
#character_3
character_3_walkup = [pygame.image.load('./sprites/character_3/U3.png'),
                      pygame.image.load('./sprites/character_3/U2.png'),
                      pygame.image.load('./sprites/character_3/U3.png'),
                      pygame.image.load('./sprites/character_3/U4.png')]
character_3_walkdown = [pygame.image.load('./sprites/character_3/D3.png'),
                        pygame.image.load('./sprites/character_3/D2.png'),
                        pygame.image.load('./sprites/character_3/D3.png'),
                        pygame.image.load('./sprites/character_3/D4.png')]
character_3_walkright = [pygame.image.load('./sprites/character_3/R3.png'),
                         pygame.image.load('./sprites/character_3/R2.png'),
                         pygame.image.load('./sprites/character_3/R3.png'),
                         pygame.image.load('./sprites/character_3/R4.png')]
character_3_walkleft = [pygame.image.load('./sprites/character_3/L3.png'),
                        pygame.image.load('./sprites/character_3/L2.png'),
                        pygame.image.load('./sprites/character_3/L3.png'),
                        pygame.image.load('./sprites/character_3/L4.png')]
#character_4
character_4_walkup = [pygame.image.load('./sprites/character_4/U4.png'),
                      pygame.image.load('./sprites/character_4/U2.png'),
                      pygame.image.load('./sprites/character_4/U3.png'),
                      pygame.image.load('./sprites/character_4/U4.png')]
character_4_walkdown = [pygame.image.load('./sprites/character_4/D4.png'),
                        pygame.image.load('./sprites/character_4/D2.png'),
                        pygame.image.load('./sprites/character_4/D3.png'),
                        pygame.image.load('./sprites/character_4/D4.png')]
character_4_walkright = [pygame.image.load('./sprites/character_4/R4.png'),
                         pygame.image.load('./sprites/character_4/R2.png'),
                         pygame.image.load('./sprites/character_4/R3.png'),
                         pygame.image.load('./sprites/character_4/R4.png')]
character_4_walkleft = [pygame.image.load('./sprites/character_4/L4.png'),
                        pygame.image.load('./sprites/character_4/L2.png'),
                        pygame.image.load('./sprites/character_4/L3.png'),
                        pygame.image.load('./sprites/character_4/L4.png')]

guessingGame = False

# paths
path1 = [(280, 280), (180, 280), (180, 430), (180,120), (180, 280), (280, 280), (280, 230), (490, 230), (490, 400)]
path2 = [(280, 510), (80, 510), (80, 280), (280, 280), (280, 400), (490, 400)]
path3 = [(280, 230), (490, 230), (490, 190), (490, 400)]
path4 = [(280, 280), (80, 280), (80, 120), (80,510), (280, 510), (280, 400), (490, 400)]
pathsList = [path1, path2, path3, path4]

# the path from the counter to the exit door
exitPath = [(280, 400), (280, 600)]


class Client(object):
    def __init__(self):
        self.characterSize  = 80, 120
        self.characterWidth = 80
        self.characterHeight = 120
        self.x = 280
        self.y = 570

        # directions
        self.up = True  # the character should enter while going up
        self.down = False
        self.right = False
        self.left = False

        # the index of which tuple is the character at when walking through a certain path
        self.pathIndex = 0

        # last direction of where the character walked so to display him standing in that direction when he stops
        self.lastDirection = "none"

        # walking speed in pixels MUST NOT BE CHANGED BECAUSE IT MATCHES WITH THE PATH TUPLES also it's looking good
        self.step = 10

        # it tells if the client is still buying so that we can start the guessing game
        self.finishedBuying = False

        # frames index, helps to display sprites from 0 to 3
        self.walkCount = 0
        self.path = random.choice(pathsList)

        characterNumber = random.choice([1, 2, 3, 4])

        if characterNumber == 1:
            self.walkUp = character_1_walkup
            self.walkDown = character_1_walkdown
            self.walkRight = character_1_walkright
            self.walkLeft = character_1_walkleft
        elif characterNumber == 2:
            self.walkUp = character_2_walkup
            self.walkDown = character_2_walkdown
            self.walkRight = character_2_walkright
            self.walkLeft = character_2_walkleft
        elif characterNumber == 3:
            self.walkUp = character_3_walkup
            self.walkDown = character_3_walkdown
            self.walkRight = character_3_walkright
            self.walkLeft = character_3_walkleft
        elif characterNumber == 4:
            self.walkUp = character_4_walkup
            self.walkDown = character_4_walkdown
            self.walkRight = character_4_walkright
            self.walkLeft = character_4_walkleft

    def draw(self):
        if self.walkCount >= 4:
            self.walkCount = 0

        # print("{} {} {} {}".format(self.up, self.down, self.right, self.left))
        if self.up:
            screen.blit(self.walkUp[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        elif self.down:
            screen.blit(self.walkDown[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            screen.blit(self.walkRight[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        elif self.left:
            screen.blit(self.walkLeft[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        else:
            if self.lastDirection == "up":
                screen.blit(self.walkUp[0], (self.x, self.y))
            elif self.lastDirection == "down":
                screen.blit(self.walkDown[0], (self.x, self.y))
            elif self.lastDirection == "right":
                screen.blit(self.walkRight[0], (self.x, self.y))
            elif self.lastDirection == "left":
                screen.blit(self.walkLeft[0], (self.x, self.y))
            else:
                screen.blit(self.walkDown[0], (self.x, self.y))
        # print(self.walkCount)

    def move_in_direction(self, direction):
        # moves the character one step in a given direction

        if direction == "up" and self.y - self.step >= 0:
            self.up = True
            self.lastDirection = "up"
            self.y -= self.step

        elif direction == "down" and self.y + self.characterHeight + self.step <= screenHeight:
            self.down = True
            self.lastDirection = "down"
            self.y += self.step

        elif direction == "right" and self.x + self.characterWidth + self.step <= screenWidth:
            self.right = True
            self.lastDirection = "right"
            self.x += self.step

        elif direction == "left" and self.x - self.step >= 0:
            self.left = True
            self.lastDirection = "left"
            self.x -= self.step

    def move_to(self, x, y):
        # uses the move_in_direction to move the character to a certain coordinates in the order right left down up

        if x <= screenWidth and self.x < x:
            self.move_in_direction("right")
        elif x >= 0 and self.x > x:
            self.move_in_direction("left")
        elif y <= screenHeight and self.y < y:
            self.move_in_direction("down")
        elif y >= 0 and self.y > y:
            self.move_in_direction("up")

    def walk_through_path(self):
        # uses move_to to move to all the coordinates in a path one after the other until the path ends

        if self.path is not None:
            if self.pathIndex < self.path.__len__():  # if the client didn't reach the end of the path (the counter)
                self.move_to(*self.path[self.pathIndex])  # he moves to the next checkpoint
                if (self.x, self.y) == (self.path[self.pathIndex]):  # if he actually reached the checkpoint
                    self.pathIndex += 1
                    # when the character arrives to the counter
                    if self.pathIndex >= self.path.__len__() and not (self.x, self.y) == (280, 600):
                        self.lastDirection = "down"  # to make the character look down when he arrives to the counter
                        self.pathIndex = 0
                        self.finishedBuying = True  # to launch the guessing game the next time in the main loop
                    # when the character is walking through the exit path and he arrives to the the exit door
                    elif (self.x, self.y) == (280, 600):
                        self.pathIndex = 0

    def leave_store(self):
        # moves the character from the counter to the exit door

        if exitPath is not None:
            if self.pathIndex < exitPath.__len__():
                self.move_to(*exitPath[self.pathIndex])
                if (self.x, self.y) == (exitPath[self.pathIndex]):
                    self.pathIndex += 1
                    # when the character is walking through the exit path and he arrives to the the exit door
                    if (self.x, self.y) == (280, 600):
                        self.pathIndex = 0

    def clear_directions(self):
        self.up = False
        self.down = False
        self.right = False
        self.left = False

class Player(object):
    def __init__(self):
        self.score = 0

def redrawGameWindow():
    # draws background, character then foreground

    clock.tick(20)
    screen.blit(background, (0, 0))
    client.draw()
    screen.blit(foreground, (0, 0))
    # Guessing game drawing should be here to come on top of the rest
    pygame.display.update()
    clock.tick(30)

def guessing_game():
    # this function should have the code of the guessing game which will set gessingGame to False when finishing

    global client

    # guessing game code should be here
    # when drawing something do it in the redrawGameWindow() and put it right before the update function call
    # you can also create a class for that and call it's drawing function from redrawGameWindow()

    client.leave_store()  # delete this after adding guessing_game code and add it when the guessing game finishes
    if (client.x, client.y) == (280, 600):
        client = None  # to generate a new client and set a new path for him
        client = Client()


client = Client()

# main loop
run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if client is None:
        client = Client()

    if not client.finishedBuying:
        client.walk_through_path()

    elif client.finishedBuying:
        guessing_game()

    redrawGameWindow()

    client.clear_directions()

# leave the game
pygame.quit()
