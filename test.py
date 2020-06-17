import pygame

pygame.init()

size = width, height = 648, 720
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255
character_size = width, height = 100, 300

#set size of the window
screen = pygame.display.set_mode(size)

background = pygame.image.load('tiles/background.png')

# set title of the window
pygame.display.set_caption("Data Mining Game")


def redraw():
    screen.blit(background, (0,0))

    # # draw a white rectangle
    # pygame.draw.rect(screen, white, (50, 50, 100, 300))

# main loop
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redraw()
    pygame.display.update()

# leave the game 
pygame.quit()
