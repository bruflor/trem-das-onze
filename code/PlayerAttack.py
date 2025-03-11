import pygame

from code.Const import ENTITY_SPEED
from code.Entity import Entity


class PlayerAttack(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.surf = pygame.image.load('./assets/'+ name +'_Shot.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])

    def move(self):
        self.rect.centerx += ENTITY_SPEED[self.name]