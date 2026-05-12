import Enemy
import pygame
import os

class Goblin(Enemy.Enemy):
    def __init__(self, x, y, platform):
        super().__init__(x, y)

        self.animations = { "move": []}
        self.speed = 3
        self.state = "move"
        self.update_time = pygame.time.get_ticks()
        self.frame_index= 0
        self.load_assets()
        self.image = self.animations[self.state][self.frame_index]
        self.flip = False

        # Posicionamiento
        self.rect = self.image.get_rect()
        self.rect.bottom = platform.top 
        self.rect.x = x

        # Movimiento
        self.platform = platform 
        self.speed = 2
        self.direction = 1

    def update(self):
            cooldown_animation = 100
            self.rect.x += self.speed * self.direction

            if self.rect.right > self.platform.right:
                self.direction = -1
                self.flip = True
            if self.rect.left < self.platform.left:
                self.direction = 1
                self.flip = False

            self.image = self.animations[self.state][self.frame_index]
            if pygame.time.get_ticks() - self.update_time >= cooldown_animation:
                self.frame_index = self.frame_index + 1
                self.update_time = pygame.time.get_ticks()
            if self.frame_index >= len(self.animations[self.state]):
                self.frame_index = 0
    
    def attack(self):
        print("¡El goblin ataca con su cimitarra!")

    def draw(self, interface, scroll):
        image_flip = pygame.transform.flip(self.image, self.flip , flip_y= False )
        interface.blit(image_flip, (self.rect.x - scroll[0], self.rect.y - scroll[1]))

    def  load_assets(self):
        root_path = "assets/images/enemies/goblin"
        for animation in self.animations.keys():
            final_path = os.path.join(root_path, animation)
            files = sorted(os.listdir(final_path))
            
            for file in files:
                if file.endswith(".png"):
                    image_path = os.path.join(final_path, file)
                    img = pygame.image.load(image_path).convert_alpha()
                    img = pygame.transform.scale(img, (64, 64))
                    self.animations[animation].append(img)

