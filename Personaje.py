import pygame # type: ignore
import constants
class Personaje():
  def __init__(self, x, y):
    self.shape = pygame.Rect(x, y, constants.PLAYER_WIDTH, constants.PLAYER_HEIGHT)
    self.shape.center = (x, y)

    self.speed = 5

  def update(self):
    pass

  def move(self, dx, dy):
    self.shape.x += dx
    self.shape.y += dy


  def atacar():
    pass
  
  def draw(self, interface):
    pygame.draw.rect(interface, constants.PLAYER_COLOR, self.shape)
