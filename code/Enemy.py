import pygame

from code.Const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOT_DELAY, WIN_HEIGHT, ENEMY_FRAME_COUNT
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.state = name
        self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()

        # Calculate the width of a single frame
        frame_width = self.surf.get_width() // ENEMY_FRAME_COUNT[name]
        frame_height = self.surf.get_height()

        # Set the rect size to match the frame size
        self.rect = self.surf.get_rect(bottomleft=position)
        self.rect.width = frame_width
        self.rect.height = frame_height

        # Physics
        self.current_frame = 0
        self.frame_rate = 10  # Frames per second
        self.frame_duration = 1000 // self.frame_rate  # Duration of each frame in milliseconds
        self.animation_timer = 0  # Track time elapsed for the current frame

        self.last_update = pygame.time.get_ticks()
        self._gravity = 0
        self.is_grounded = True  # Track if the player is on the ground

        # Images and sounds
        self.animations = {
            name: self._load_animation(f'./assets/{name}.png', frame_count=ENEMY_FRAME_COUNT[name], direction='backward'),
        }
        self.surf = self.animations[self.state][self.current_frame]  # Initial frame

    def update_animation(self, time_passed: int):
        # Update the animation timer
        self.animation_timer += time_passed

        # Check if it's time to advance to the next frame
        if self.animation_timer >= self.frame_duration:
            self.animation_timer = 0  # Reset the timer
            self.current_frame = (self.current_frame + 1) % len(self.animations[self.state])
            self.surf = self.animations[self.state][self.current_frame]

    def move(self):
        # Speed
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def update(self, time_passed):
        self.move()
        self.update_animation(time_passed)

