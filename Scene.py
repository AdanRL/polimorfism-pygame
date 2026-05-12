import pygame

class Scene:
    def __init__(self, platform_data):

        self.platform = []
        for p in platform_data:
            self.platform.append(pygame.Rect(p))
        
        self.color_ground = (100, 100, 100) # Gris
        self.font = pygame.font.SysFont("Arial", 22, bold=True)
        self.controles_txt = self.font.render("CONTROLES: A-D Mover | Espacio: Saltar | E: Atacar", True, (200, 200, 200))

    def draw(self, interface, scroll):
        # 1. Dibujar el texto (Tutorial)
        # Nota: NO le restamos el scroll para que el texto se quede fijo en la pantalla (HUD)
        interface.blit(self.controles_txt, (50, 50))
        
        # 2. Dibujar las plataformas con scroll
        for p in self.platform:
            # Creamos un rectángulo temporal desplazado para el dibujo
            # Restamos el scroll a la X y a la Y
            rect_desplazado = pygame.Rect(p.x - scroll[0], p.y - scroll[1], p.width, p.height)
            pygame.draw.rect(interface, self.color_ground, rect_desplazado)

    def get_platform(self):
        return self.platform
