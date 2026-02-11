import pygame
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((626,351))
pygame.display.set_caption("game")
icon = pygame.image.load('banned_18246125.png')

pygame.display.set_icon(icon)

bg = pygame.image.load("on display.jpeg")
player = pygame.image.load("player/Left 1.png")
walk_left = [
    pygame.image.load("player/Left 1.png"),
    pygame.image.load("player/Left 2.png"),
    pygame.image.load("player/Left 3.png"),
    pygame.image.load("player/Left 4.png")
]
walk_right = [
    pygame.image.load("player/rigtht 1.png"),
    pygame.image.load("player/rigtht 2.png"),
    pygame.image.load("player/rigtht 3.png"),
    pygame.image.load("player/rigtht 4.png")
]

player_anim_count = 0
bg_x = 0

player_speed = 5
player_x = 150
player_y = 250

is_jumping = False
jumping_count = 7


bg_sound = pygame.mixer.Sound("sound/dora_-_Dora_dura_67181158.mp3")
bg_sound.play()
running = True
while running:
    
    
    screen.blit(bg,(bg_x,0))
    screen.blit(bg,(bg_x + 626,0))
    screen.blit(walk_left[player_anim_count],(player_x,250))
    if player_anim_count == 3:
        player_anim_count = 0
    
        
        
    key = pygame.key.get_pressed()
    
    if key[pygame.K_LEFT]:
        screen.blit(walk_left[player_anim_count],(player_x,player_y))
    else:
        screen.blit(walk_right[player_anim_count],(player_x,player_y))
    
    if not(is_jumping):
        if key[pygame.K_SPACE]:
            is_jumping = True
        else:
            if jumping_count >= -7:
                if jumping_count < 0:
                    player_y += (jumping_count ** 2) /2
                else:
                    player_y = (jumping_count ** 2) /2 
                    jumping_count -= 1
            else:
                is_jumping = False
                jumping_count = 7   
                
  
    
    if key[pygame.K_LEFT]and player_x > 0:
        player_x -= player_speed
    elif key[pygame.K_RIGHT]and player_x <500:
        player_x += player_speed
    else:
        player_anim_count += 1 
        
        bg_x -= 2
        if bg_x == 626:
            bg_x = 0
            
            
        
        
    
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            
            
            
    clock.tick(10)
            
          