import pygame
import constants
import os

class Personaje():
	def __init__(self, x, y):

		self.animations = {"attack": [], "move": [], "idle": [], "jump": []}
		self.speed = 3
		self.state = "idle"
		self.frame_index= 0
		self.update_time = pygame.time.get_ticks()
		self.flip = False

		self.vel_y = 0 
		self.is_jumping = False 
		self.gravity = 1         
		self.jump_force = -20   

		self.is_attacking = False
		self.attack_cooldown = 0

		self.load_assets()
		self.image = self.animations[self.state][self.frame_index]
		self.shape = pygame.Rect(0,0, constants.PLAYER_WIDTH, constants.PLAYER_HEIGHT)
		self.rect = self.image.get_rect()



	def update(self):

		if self.state == "idle":
			cooldown_animation = 450
		else:
			cooldown_animation = 100
			
		self.image = self.animations[self.state][self.frame_index]
		if pygame.time.get_ticks() - self.update_time >= cooldown_animation:
			self.frame_index = self.frame_index + 1
			self.update_time = pygame.time.get_ticks()
		if self.frame_index >= len(self.animations[self.state]):
			if self.is_attacking:
				self.is_attacking = False
			self.frame_index = 0
			

	def move(self, dx, dy):
		self.shape.x += dx
		
		# --- Límite Izquierdo ---
		if self.shape.left < 0:
			self.shape.left = 0
			
		# --- Límite Derecho ---
		if self.shape.right > constants.WINDOW_WIDTH:
			self.shape.right = constants.WINDOW_WIDTH

		self.shape.y += dy
		
		# --- Límite Superior ---
		if self.shape.top < 0:
			self.shape.top = 0
			self.vel_y = 0 
			
		# --- Límite Inferior---
		if self.shape.bottom > constants.WINDOW_HEIGHT:
			self.shape.bottom = constants.WINDOW_HEIGHT
			self.is_jumping = False
			self.vel_y = 0

		self.rect.center = self.shape.center

	def get_attack_rect(self):
		# cuadrado de colisiones
		if self.flip: # Atacando a la izquierda
			return pygame.Rect(self.shape.x - 40, self.shape.y, 40, self.shape.height)
		else: # Atacando a la derecha
			return pygame.Rect(self.shape.right, self.shape.y, 40, self.shape.height)
	
	def atacar(self):
		if not self.is_attacking:
			self.is_attacking = True
			self.state = "attack"
			self.frame_index = 0

	def  load_assets(self):
		root_path = "assets/images/player"
		for animation in self.animations.keys():
			final_path = os.path.join(root_path, animation)
			files = sorted(os.listdir(final_path))

			for file in files:
				if file.endswith(".png"):
					image_path = os.path.join(final_path, file)
					img = pygame.image.load(image_path).convert_alpha()
					img = pygame.transform.scale(img, (64, 64))
					self.animations[animation].append(img)

	
	def apply_gravity(self, platforms):
		# Aplicar gravedad
		self.vel_y += self.gravity
		self.shape.y += self.vel_y

		# Comprobar colisión con cada plataforma
		for platform in platforms:
			if self.shape.colliderect(platform):
				if self.vel_y > 0:
					self.shape.bottom = platform.top
					self.vel_y = 0
					self.is_jumping = False

	def jump(self):
		if not self.is_jumping: 
			self.vel_y = self.jump_force
			self.is_jumping = True
			self.state = "jump" 
			self.frame_index = 0

	def draw(self, interface):
			image_flip = pygame.transform.flip(self.image, self.flip , flip_y= False )
			interface.blit(image_flip, self.shape)
			# pygame.draw.rect(interface, constants.PLAYER_COLOR, self.shape)
