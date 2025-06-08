import pygame

#initialize Pygame
pygame.init()

#Set up screen dimensions
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

#Set up colors
black = (0, 0, 0)

#Clear the screen
screen.fill((255, 255, 255))

#Draw coordinate axes
pygame.draw.line(screen, black, (0, height // 2), (width, height // 2), 1)
pygame.draw.line(screen, black, (width // 2, 0), (width // 2, height), 1)

#Update the display
pygame.display.flip()

#Wait for a key event
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#Quit Pygame
pygame.quit()


