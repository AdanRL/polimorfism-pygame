import Enemy
import pygame # type: ignore

class Goblin(Enemy.Enemy):
    def __init__(self, x, y, platform):
        super().__init__(x, y)

        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 255, 0)) # Verde

        # Posicionamiento
        self.rect = self.image.get_rect()
        self.rect.bottom = platform.top 
        self.rect.x = x

        # Movimiento
        self.platform = platform 
        self.speed = 2
        self.direction = 1

    def update(self):
            # Mover horizontalmente
            self.rect.x += self.speed * self.direction

            # Lógica de patrulla: Detectar bordes de la platform
            if self.rect.right > self.platform.right:
                self.direction = -1
            if self.rect.left < self.platform.left:
                self.direction = 1
    
    def attack(self):
        print("¡El goblin ataca con su cimitarra!")

    def draw(self, interface):
        interface.blit(self.image, self.rect)

