import pygame # type: ignore

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, imagePath):
        super().__init__()
        self.image = pygame.image.load(imagePath).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # STATS
        self.ca = 0
        self.iniciative = 0
        self.pg = 0
        self.speed = 0
        self.strength = 0
        self.agility = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.constitution = 0

    def update(self):
        pass
    
    def atacar():
        pass
