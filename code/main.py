import pygame

#general setup
pygame.display.set_caption('Space Shooter')
pygame.init()                                                                               #initialises pygame
Window_Width,Window_Height = 1280, 720                                                      #makes window
display_surface = pygame.display.set_mode((Window_Width, Window_Height))
running = True


while running:                                                                              #beeing abel to close the game
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw game
    #fill window with color
    display_surface.fill('grey14')
    pygame.display.update()                                                                 #can use .flip too, which lets you specify what should be updated



pygame.quit()