import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        pygame.Surface.fill(screen, color=(0,0,0))

        #Making the window close if the user pressed the [QUIT] button.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return









        pygame.display.flip()




if __name__ == "__main__":
    main()