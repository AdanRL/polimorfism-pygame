import Enemy
import pygame # type: ignore

class RedDragon(Enemy.Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, "assets/dragon_rojo.png")

        self.image = pygame.transform.scale(self.image, (x, y))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 4

        # STATS
        self.ca = 18
        self.iniciative = 0
        self.pg = 256
        self.speed = 4
        self.strength = 27
        self.agility = 10
        self.intelligence = 16
        self.wisdom = 13
        self.charisma = 15
        self.constitution = 20

    def update(self):
        print("¡El dragon rojo vuela")
    
    def attack(self):
        print("¡El dragon rojo lanza su aliento de fuego!")

