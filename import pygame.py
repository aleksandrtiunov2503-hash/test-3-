import pygame
pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("game")
icon = pygame.image.load('изображение 1/banned_18246125.png')

pygame.display.set_icon(icon)

player = pygame.image.load("изображение 1/banned_18246125.png")




running = True
while running:

    screen.blit(player,(600,300))
    
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()