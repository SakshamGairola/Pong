import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def Move(self, change):
        self.rect.y += change
        if self.rect.y < 5:
            self.rect.y = 5
        elif self.rect.y > 565:
            self.rect.y = 565