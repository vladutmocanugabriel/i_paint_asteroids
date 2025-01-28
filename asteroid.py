import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
      pygame.draw.circle(surface=screen, color="white", center = self.position, radius = self.radius , width=2)

    def update(self, dt):
       self.position += self.velocity * dt

    def split(self):
       self.kill()
       if self.radius <= ASTEROID_MIN_RADIUS:
          return
       else:
          random_angle = random.uniform(20, 50)
          asteroid_one = Asteroid(self.position.x, self.position.y, radius= self.radius - ASTEROID_MIN_RADIUS)
          asteroid_two = Asteroid(self.position.x, self.position.y, radius= self.radius - ASTEROID_MIN_RADIUS)
          asteroid_one.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle) * 1.2
          asteroid_two.velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle) * 1.2