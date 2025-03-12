import pygame

from code.Const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOT_DELAY, WIN_HEIGHT, FRAME_COUNT
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        # Physics
        self.frame_duration = 1000 // self.frame_rate  # Duration of each frame in milliseconds
        self.animation_timer = 0  # Track time elapsed for the current frame

        # # Images and sounds
        self.animations = {
            self.image: self._load_animation(f'./assets/{name}.png', frame_count=FRAME_COUNT[self.image],
                                             direction='backward'),
        }

    def update_animation(self, time_passed: int):
        # Update the animation timer
        self.animation_timer += time_passed

        # Check if it's time to advance to the next frame
        if self.animation_timer >= self.frame_duration:
            self.animation_timer = 0  # Reset the timer
            self.current_frame = (self.current_frame + 1) % len(self.animations[self.image])
            self.surf = self.animations[self.image][self.current_frame]

    def move(self):
        # Speed
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def update(self, time_passed):
        self.move()
        self.update_animation(time_passed)
