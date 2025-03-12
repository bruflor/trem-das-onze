from abc import ABC, abstractmethod
import pygame

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE, WIN_WIDTH, WIN_HEIGHT, FRAME_COUNT


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.last_dmg = 'None'
        self.score = ENTITY_SCORE[self.name]
        self.frame_rate = 10  # Frames per second
        self.collided_with = set()  # Track entities that have already collided with this entity

        # Images
        self.current_frame = 0
        self.state = 'walking'
        self.image = f'{self.name}_{self.state}'
        self.animations = {
            self.image: self._load_animation(f'./assets/{name}.png', frame_count=FRAME_COUNT[self.image]),
        }
        self.surf = self.animations[self.image][self.current_frame]  # Initial frame

        frame_width = self.surf.get_width() // FRAME_COUNT[self.image]
        frame_height = self.surf.get_height()
        self.rect = self.surf.get_rect(bottomleft=position)
        self.rect.width = frame_width
        self.rect.height = frame_height

    def _load_animation(self, path: str, frame_count: int, direction='None'):
        # Load a spritesheet and cut the frames
        spritesheet = pygame.image.load(path).convert_alpha()
        if direction == "backward":
            sprite = pygame.transform.flip(spritesheet, True, False)
            spritesheet = sprite
        frame_width = spritesheet.get_width() // frame_count
        frame_height = spritesheet.get_height()
        frames = []
        for i in range(frame_count):
            frame = spritesheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            frames.append(frame)
        return frames


# Decorator to method
@abstractmethod
def update_animation(self):
    pass

# Decorator to method
@abstractmethod
def move(self):
    pass
