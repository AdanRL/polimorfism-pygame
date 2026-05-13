import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self, x, y, direccion):
        super().__init__()
        # Representación visual: cuadrado rojo
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        
        # Física del proyectil
        self.speed_x = 5 * direccion  # Dirección es 1 o -1
        self.vel_y = -10              # Impulso inicial hacia arriba para la parábola
        self.gravity = 0.5            # Gravedad que lo hará caer

    def update(self):
        # Movimiento parabólico
        self.rect.x += self.speed_x
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        # Eliminar si sale de la pantalla (ajusta según tu ventana)
        if self.rect.y > 600 or self.rect.x < -100 or self.rect.x > 2000:
            self.kill()

    def draw(self, interface, scroll):
        interface.blit(self.image, (self.rect.x - scroll[0], self.rect.y - scroll[1]))