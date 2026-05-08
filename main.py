
import constants
import pygame # type: ignore
import Personaje

def main():
  pygame.init()
  screen = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
  pygame.display.set_caption("Polimorfismo en Pygame")
  clock = pygame.time.Clock()
  player = Personaje.Personaje(constants.PLAYER_WIDTH, constants.PLAYER_HEIGHT)

  move_top = False
  move_bottom = False
  move_left = False
  move_right = False

  run = True
  while run:
    clock.tick(constants.FPS)
    screen.fill(constants.BG_COLOR)
    player.draw(screen)

    if move_top:
      player.move(0, -player.speed)
    if move_bottom:
      player.move(0, player.speed)
    if move_left:
      player.move(-player.speed, 0)
    if move_right:
      player.move(player.speed, 0)
    
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
        if event.key == pygame.K_w:
          move_top = True

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
