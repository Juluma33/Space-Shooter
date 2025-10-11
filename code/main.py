import pygame
from os.path import join #better game directioanry cause / != \
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self, Groups):
        super().__init__(Groups)
        self.image = pygame.image.load(join('images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center = (Window_Width / 2, Window_Height / 2))
        self.direction = pygame.Vector2()
        self.speed = 300
    
    def update(self, delta_time):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * delta_time
        
        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE]:
            print("fire laser")

class Stars(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (randint(0, Window_Width), randint(0, Window_Height)))

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

all_sprites = pygame.sprite.Group()
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
for i in range(20):
    Stars(all_sprites, star_surf)
player = Player(all_sprites)

meteor_surface = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surface.get_frect(center = (Window_Width / 2, Window_Height / 2))

laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, Window_Height - 20))

while running:
    #framerate
    delta_time = clock.tick() / 1000    # /1000 for seconds
    
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    all_sprites.update(delta_time)
    
    #draw game
    display_surface.fill('darkgrey')
    all_sprites.draw(display_surface)
    
    pygame.display.update()



pygame.quit()