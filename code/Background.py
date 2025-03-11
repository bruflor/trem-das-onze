import pygame

from code.Const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT, ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE
from code.Entity import Entity


class Background:
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()
        scaled_img = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.surf = scaled_img
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.last_dmg = 'None'
        self.score = ENTITY_SCORE[self.name]


    def move(self):
        pass
        # Speed
        self.rect.centerx -= ENTITY_SPEED[self.name]
        # When the image is on the end of the right corner, put it to restart
        if self.rect.right  <= 0:
            self.rect.left = WIN_WIDTH