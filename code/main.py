import pygame
from os.path import join #better game directioanry cause / != \
from random import randint


#general setup
pygame.init()
Window_Width,Window_Height = 1280, 720
display_surface = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption('Space Shooter')
running = True
clock = pygame.time.Clock()

#plain surface
surf = pygame.Surface((100,200))
surf.fill('orange')
x = 100

#imports
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (Window_Width / 2, Window_Height / 2))
player_direction = pygame.math.Vector2(1, 0)
player_speed = 300

star_surface = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [(randint(0, Window_Width), randint(0, Window_Height)) for i in range(20)]

meteor_surface = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surface.get_frect(center = (Window_Width / 2, Window_Height / 2))

laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, Window_Height - 20))

while running:
    #framerate
    delta_time = clock.tick() / 1000
    
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #draw game
    #fill window with color
    display_surface.fill('darkgrey')
    for pos in star_positions:
        display_surface.blit(star_surface, pos)
    
    display_surface.blit(meteor_surface, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)
    
    #player movement
    player_rect.center += player_direction * player_speed * delta_time
    display_surface.blit(player_surf, player_rect)
    
    
    
    pygame.display.update()



pygame.quit()