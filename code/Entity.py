from abc import ABC, abstractmethod
import pygame

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE, WIN_WIDTH, WIN_HEIGHT


class Entity(ABC):
    def __init__(self, name:str, position:tuple):
        self.name = name
        # self.surf = pygame.image.load('./assets/'+ name +'.png').convert_alpha()
        # scaled_img = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        # self.surf = scaled_img
        # self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.last_dmg = 'None'
        self.score = ENTITY_SCORE[self.name]
        self.collided_with = set()  # Track entities that have already collided with this entity



    # Decorator to method
    @abstractmethod
    def move(self):
        pass

