
import RedDragon
import pygame # type: ignore


def main():

  # pygame setup
  pygame.init()
  screen = pygame.display.set_mode((1280, 720))
  clock = pygame.time.Clock()
  running = True

  player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
  red_dragon = RedDragon.RedDragon(150, 150)

  enemies = pygame.sprite.Group()
  enemies.add(red_dragon)
  
  while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    last_position_x = player_pos.x
    last_position_y = player_pos.y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    # 3. CREAR LA CAJA DE COLISIÓN PARA TU CÍRCULO
    player_rect = pygame.Rect(player_pos.x - 40, player_pos.y - 40, 80, 80)
    has_collided = False
    
    for enemigo in  enemies:
        if player_rect.colliderect(enemigo.rect):
            has_collided = True
            break


    if has_collided:
      player_pos.x = last_position_x
      player_pos.y = last_position_y

    pygame.draw.circle(screen, "red", player_pos, 40)
    enemies.draw(screen)
      # flip() the display to put your work on screen
    pygame.display.flip()

      # limits FPS to 60
      # dt is delta time in seconds since last frame, used for framerate-
      # independent physics.
    dt = clock.tick(60) / 1000

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()


if __name__ == "__main__":    main()
