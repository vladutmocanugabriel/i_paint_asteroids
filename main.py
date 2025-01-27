import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_management = pygame.time.Clock()
    dt = 0

    #Creating object groups to manage the player and asteroids
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    #Creating the player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        #Making the window close if the user pressed the [QUIT] button.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Filling the screen with black color.    
        pygame.Surface.fill(screen, color=(0,0,0))




        for obj in updatable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)

        # #Update the movement of the player.
        # player.update(dt)
        # #Drawing the player and rendering him each frame.
        # player.draw(screen)
        














        #Limit the framerate to 60 FPS
        dt = fps_management.tick(60) / 1000
        
        pygame.display.flip()




if __name__ == "__main__":
    main()