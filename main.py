
import constants
import pygame
import Personaje
import Scene
import Goblin
import Warrior
	
def main():
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load("assets/audio/background_music.mp3")
	pygame.mixer.music.play(-1)
	pygame.mixer.music.set_volume(0.5)

	screen = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
	pygame.display.set_caption("Tarea de Pygamed ")
	clock = pygame.time.Clock()
	player = Personaje.Personaje(constants.PLAYER_WIDTH, constants.PLAYER_HEIGHT)

	move_top = False
	move_bottom = False
	move_left = False
	move_right = False
	run = True

	scene_data= [
		(0, 500, 1600, 20),
		(200, 380, 150, 20),
		(450, 280, 150, 20),
		(550, 180, 150, 20)
	]

	level1 = Scene.Scene(scene_data)
	goblin_platform = level1.get_platform()[1]
	goblin1 = Goblin.Goblin(300, 0, goblin_platform)
	warrior1 = Warrior.Warrior(1200, 400)

	enemies = pygame.sprite.Group()
	weapons = pygame.sprite.Group()
	enemies.add(goblin1)
	enemies.add(warrior1)

	scroll = [0, 0]
	
	while run:
		screen.fill(constants.BG_COLOR)
		clock.tick(constants.FPS)
		player.apply_gravity(level1.get_platform())

		scroll[0] += (player.shape.x - scroll[0] - constants.WINDOW_WIDTH // 2) / 15
		scroll[1] += (player.shape.y - scroll[1] - constants.WINDOW_HEIGHT // 2) / 15
		scroll_int = [int(scroll[0]), int(scroll[1])]
		level1.draw(screen, scroll_int)
		player.draw(screen, scroll)
		player.update()

		enemies.update()

		if player.is_attacking:
			rect_ataque = player.get_attack_rect()
			pygame.draw.rect(screen, (255, 0, 0), 
                     (rect_ataque.x - scroll_int[0], 
                      rect_ataque.y - scroll_int[1], 
                      rect_ataque.width, rect_ataque.height), 2)

			for goblin in enemies:
				if rect_ataque.colliderect(goblin.rect):
					goblin.kill()

		for enemy in enemies:
			enemy.draw(screen, scroll)
			if isinstance(enemy, Warrior.Warrior):
						enemy.ai(player.shape)
			elif isinstance(enemy, Goblin.Goblin):
						enemy.throw(weapons)
		weapons.update()

		for weapon in weapons:
			weapon.draw(screen, scroll_int)

		if player.is_attacking:
			new_state = "attack"
		elif player.is_jumping:
			new_state = "jump"
		elif move_left or move_right or move_top or move_bottom:
			new_state ="move"
		else:
			new_state = "idle"

		if new_state != player.state:
			player.state = new_state
			player.frame_index = 0

		if move_left:
			player.move(-player.speed, 0)
			player.flip = True
		if move_right:
			player.move(player.speed, 0)
			player.flip = False
		if move_top:
			player.move(0, -player.speed)
		if move_bottom:
			player.move(0, player.speed)

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					move_left = True
				if event.key == pygame.K_s:
					move_bottom = True
				if event.key == pygame.K_d:
					move_right = True
					player.flip = False
				if event.key == pygame.K_w:
					move_top = True
				if event.key == pygame.K_SPACE:
					player.jump()
				if event.key == pygame.K_e: 
					player.atacar()
		
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a:
					move_left = False
				if event.key == pygame.K_s:
					move_bottom = False
				if event.key == pygame.K_d:
					move_right = False
				if event.key == pygame.K_w:
					move_top = False

		pygame.display.update()

if __name__ == "__main__":    main()
