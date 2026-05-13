import pygame
import Enemy
import os
import math

class Warrior(Enemy.Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = 3
        self.health = 3
        self.state = "move"
        self.flip = False
        
        # Rango de visión y de ataque
        self.detection_range = 400
        self.attack_range = 50
        
        # Cargar assets (reutiliza tu lógica de load_assets)
        self.animations = {"move": [], "attack": []}
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.load_assets()
        self.image = self.animations[self.state][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x, y))

    def ai(self, player_rect):
        # Calcular distancia al jugador
        dist_x = player_rect.centerx - self.rect.centerx
        
        if abs(dist_x) < self.detection_range:
            # Si está en rango de ataque
            if abs(dist_x) < self.attack_range:
                self.state = "attack"
            else:
                # Perseguir
                self.state = "move"
                if dist_x > 0:
                    self.rect.x += self.speed
                    self.flip = False
                else:
                    self.rect.x -= self.speed
                    self.flip = True
        else:
            self.state = "move"

    def update(self):
        # Lógica de animación
        cooldown = 100
        self.image = self.animations[self.state][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        
        if self.frame_index >= len(self.animations[self.state]):
            self.frame_index = 0
            if self.state == "attack":
                self.state = "move"

    def draw(self, interface, scroll):
        img = pygame.transform.flip(self.image, self.flip, False)
        interface.blit(img, (self.rect.x - scroll[0], self.rect.y - scroll[1]))

    def  load_assets(self):
        root_path = "assets/images/enemies/warrior"
        for animation in self.animations.keys():
            final_path = os.path.join(root_path, animation)
            files = sorted(os.listdir(final_path))
            
            for file in files:
                if file.endswith(".png"):
                    image_path = os.path.join(final_path, file)
                    img = pygame.image.load(image_path).convert_alpha()
                    img = pygame.transform.scale(img, (64, 64))
                    self.animations[animation].append(img)