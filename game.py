import random
from random import choice, randint
from apriori import Apriori
import pygame

pygame.init()
pygame.font.init()
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

#load then play music permanently
music = pygame.mixer.music.load("bgm.wav")
pygame.mixer.music.play(-1)

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
num_transaction = 0
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

# compte le nombre d'element communs entre deux tableaux
def count(tab1, tab2):
    count = 0
    for i in range(0, len(tab1)):
        for j in range(0, len(tab2)):
            if tab1[i] == tab2[j] :
                count+=1
    return count

# fonction qui retourne l'indice du tableau qui contient le plus d'elements communs
def search_index(tab1, tab2):
    index = randint(0, len(tab1)-1)
    nbr_common_elements = 0
    for i in range(0, len(tab1)):
        nbr = count(tab1[i], tab2)
        if(nbr > nbr_common_elements) :
            nbr_common_elements = nbr
            index = i
    return index

# fonction qui retourne le choix de l'algorithme apriori
def choice_apriori():
    global known_objects
    global choices
    global antecedents
    global consequents
    index = search_index(antecedents, known_objects)
    choice = search_index(choices, consequents[index])
    return choice

def draw_score():
    global score_player
    global score_algo
    font = pygame.font.SysFont('Arial', 18)
    font.set_bold(True)
    text3 = font.render('SCORE DU JOUEUR : '+str(score_player), False, (47,60,126), (251,234,235))
    text4 = font.render("SCORE DE L'ALGORITHME APRIORI : "+str(score_algo), False, (47,60,126), (251,234,235))
    screen.blit(text3, (50,50))
    screen.blit(text4, (50,80))



def redrawGameWindow():
    # draws background, character then foreground
    global guessingGame
    clock.tick(20)
    screen.blit(background, (0, 0))
    client.draw()
    screen.blit(foreground, (0, 0))
    draw_score()
    if guessingGame == True :
        draw_choice()
    pygame.display.update()
    clock.tick(30)

def draw_choice():
    global num_transaction
    global unknown_transactions
    global number_known_objects
    global number_unknown_objects
    global known_objects
    global unknown_objects
    global choices
    global is_drawn
    global guessingGame
    global right_choice_id
    global left_circle
    global right_circle
    global score_algo
    global score_player
    global enchainement_player
    global enchainement_algo
    global score_is_calculated
    objects = ['biscuit','fish','mushroom','burger',
               'fruits','pistachio','cheese','honey',
               'pizza','chicken','icecream','shrimp',
               'chocolate','meat','soda','croissant',
               'medicine','sweets','egg','milk',
               'vegetables']
    transaction = unknown_transactions[num_transaction]
    # on dessine les bulles des choix
    font = pygame.font.SysFont('Comic Sans MS', 25)
    font.set_bold(True)
    text1 = font.render('Le client a acheté :', False, (220,20,60), (255,250,205))
    text2 = font.render("Deviner ce qu'il a acheté aussi :", False, (220,20,60), (255,250,205))
    screen.blit(text1, (170, 120))
    screen.blit(text2, (100, 345))
    choice_image = pygame.image.load('tiles/choice.png')
    screen.blit(choice_image, (200, 150))
    screen.blit(choice_image, (350, 370))
    screen.blit(choice_image, (50, 370))
    # on dessine les objets sur les bulles
    if is_drawn == False :
        number_known_objects = randint(1,len(transaction))
        if number_known_objects > 4 :
            number_known_objects -= 1
        number_unknown_objects = len(transaction)-number_known_objects
        known_objects = []
        unknown_objects = []
        for i in range(0, len(transaction)):
            if(i<number_known_objects):
                known_objects.append(transaction[i])
            else:
                unknown_objects.append(transaction[i])
        print("Le client a acheté : ", known_objects)
        false_choice = []
        choices = []
        # on crée le vecteur des choix possible
        if(randint(0,10)<5):
            # on ajoute le bon choix d'abord
            choices.append(unknown_objects)
            right_choice_id = 0
            # puis on ajoute au hasard un autre choix
            false_choice.append(choice(objects))
            false_choice.append(choice(objects))
            choices.append(false_choice)
        else :
            # on ajoute au hasard un choix faux
            false_choice.append(choice(objects))
            false_choice.append(choice(objects))
            choices.append(false_choice)
            # puis on ajoute le bon choix
            choices.append(unknown_objects)
            right_choice_id = 1
        is_drawn = True

    # on calcule le score (une seule fois d'ou l'utilisation de cette condition)
    if (right_circle or left_circle) and score_is_calculated == False :
        if right_circle :
            player_choice = 0
        else :
            player_choice = 1
        old_score_player = score_player
        if(player_choice == right_choice_id) :
            if(enchainement_player == True):
                score_player *= 2
            else :
                score_player += 20
        print("score = ",score_player)
        if(old_score_player==score_player) :
            enchainement_player = False
        else :
            enchainement_player = True
        score_is_calculated = True
        # L'algo devine la liste d'achats
        algo_choice = choice_apriori()
        print("L'algo a choisi : ", choices[algo_choice])
        old_score_algo = score_algo
        if(algo_choice == right_choice_id):
            print("c'est juste ! ",end='')
            if(enchainement_algo == True):
                score_algo *= 2
            else :
                score_algo += 20
        else :
            print("faux !",end='')
        if(old_score_algo==score_algo):
            enchainement_algo = False
        else :
            enchainement_algo = True

    if right_circle and right_choice_id == 0:
        choice_image = pygame.image.load('tiles/right_choice.png')
        screen.blit(choice_image, (350, 370))
    elif left_circle and right_choice_id == 1:
        choice_image = pygame.image.load('tiles/right_choice.png')
        screen.blit(choice_image, (50, 370))
    elif right_circle and right_choice_id == 1:
        choice_image = pygame.image.load('tiles/bad_choice.png')
        screen.blit(choice_image, (350, 370))
    elif left_circle and right_choice_id == 0:
        choice_image = pygame.image.load('tiles/bad_choice.png')
        screen.blit(choice_image, (50, 370))
    # on dessine dans la première bulle
    for i in range(0, number_known_objects):
        str = 'tiles/'+known_objects[i]+'.png'
        image_known_objects = pygame.image.load(str)
        if i>=2 :
            screen.blit(image_known_objects, (290, 170+70*(i-2)))
        else :
            screen.blit(image_known_objects, (220, 170+70*i))
    # on dessine dans la deuxième bulle
    for i in range(0, len(choices[0])):
        str = 'tiles/'+choices[0][i]+'.png'
        image_known_objects = pygame.image.load(str)
        if i>=2 :
            screen.blit(image_known_objects, (430, 390+70*(i-2)))
        else :
            screen.blit(image_known_objects, (360, 390+70*i))
    # on dessine dans la troisième bulle
    for i in range(0, len(choices[1])):
        str = 'tiles/'+choices[1][i]+'.png'
        image_known_objects = pygame.image.load(str)
        if i>=2 :
            screen.blit(image_known_objects, (130, 390+70*(i-2)))
        else :
            screen.blit(image_known_objects, (60, 390+70*i))


def guessing_game():
    # this function should have the code of the guessing game which will set gessingGame to False when finishing
    global client
    global guessingGame
    global num_transaction
    global is_drawn
    global left_circle
    global right_circle
    global score_is_calculated
    guessingGame = True
    if left_circle or right_circle :
        client.leave_store()
        if (client.x, client.y) == (280, 600):
            left_circle = False
            right_circle = False
            guessingGame = False
            client = None  # to generate a new client and set a new path for him
            num_transaction += 1
            is_drawn = False
            score_is_calculated = False
            client = Client()

client = Client()
apriori = Apriori()
antecedents, consequents = apriori.get_rules()
known_transactions = apriori.get_known_transactions()
unknown_transactions = [
('milk','chocolate','croissant'),
('burger','pizza','icecream'),
('soda','icecream','pistachio'),
('chocolate','pistachio','honey'),
('shrimp','fish','sweets'),
('mushroom','medicine'),
('cheese','chicken','fruits','meat'),
('icecream','burger','pizza'),
('milk','biscuit','egg'),
('shrimp','sweets','fish'),
('honey','chocolate','pistachio'),
('medicine','mushroom'),
('burger','pizza','icecream'),
('milk','biscuit','egg'),
('pistachio','honey','chocolate'),
('chocolate','croissant','milk'),
('medicine','mushroom'),
('milk','chocolate','croissant')
]
number_known_objects = 0
number_unknown_objects = 0
known_objects = []
unknown_objects = []
choices = []
is_drawn = False
right_choice_id = -1
right_circle = False
left_circle = False
score_player = 0
score_algo = 0
enchainement_player = False
enchainement_algo = False
score_is_calculated = False
# main loop
run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if guessingGame == True :
                pos = pygame.mouse.get_pos()
                # on verifie si le joueur a cliqué sur le cercle droit
                if((pos[0] - 454)**2 + (pos[1] - 441)**2 < 93**2):
                    right_circle = True
                # on verifie si le joueur a cliqué sur le cercle gauche
                elif ((pos[0] - 153)**2 + (pos[1] - 441)**2 < 93**2):
                    left_circle = True

    if client is None:
        client = Client()

    if not client.finishedBuying:
        client.walk_through_path()

    elif client.finishedBuying:
         guessing_game()
         if num_transaction > len(unknown_transactions)-1:
             break

    redrawGameWindow()

    client.clear_directions()

# leave the game
pygame.quit()
