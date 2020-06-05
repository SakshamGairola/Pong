import pygame
from random import randint

class Ballinit(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        pygame.draw.circle(self.image, color, [400, 300], 5)
        self.rect = self.image.get_rect()
        self.velocity = [2, 2]

    def Update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
    
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)

    def colliderect(self, sprite):
        return self.rect.colliderect(sprite.rect)