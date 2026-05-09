import pygame

class Scene:
    def __init__(self, platform_data):

        self.platform = []
        for p in platform_data:
            self.platform.append(pygame.Rect(p))
        
        self.color_ground = (100, 100, 100) # Gris
        self.font = pygame.font.SysFont("Arial", 22, bold=True)
        self.controles_txt = self.font.render("CONTROLES: A-D Mover | Espacio: Saltar | E: Atacar", True, (200, 200, 200))

    def draw(self, interface):
        interface.blit(self.controles_txt, (50, 50))
        for platform in self.platform:
            pygame.draw.rect(interface, self.color_ground, platform)

    def get_platform(self):
        return self.platform