import pygame
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((626,351))
pygame.display.set_caption("game")
icon = pygame.image.load('изображение/banned_18246125.png')

pygame.display.set_icon(icon)

bg = pygame.image.load("изображение/on display.jpeg")
player = pygame.image.load("изображение/player/Left 1.png")
walk_left = [
    pygame.image.load("изображение/player/Left 1.png"),
    pygame.image.load("изображение/player/Left 2.png"),
    pygame.image.load("изображение/player/Left 3.png"),
    pygame.image.load("изображение/player/Left 4.png")
]
"""walk_right = [
    pygame.image.load("изображение/player/right1.png"),
    pygame.image.load("изображение/player/right2.png"),
    pygame.image.load("изображение/player/right3.png"),
    pygame.image.load("изображение/player/right4.png")
]
"""
player_anim_count = 0
bg_x = 0
running = True
while running:
    
    
    screen.blit(bg_x,(bg_x,0))
    screen.blit(bg,(bg_x + 626,0))
    screen.blit(walk_left[player_anim_count],(300,250))
    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1 
        
        bg_x = -2
        if bg_x == 626:
            bg_x = 0 
    
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            
            
            
    clock.tick(10)
            
          