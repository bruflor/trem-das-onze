import pygame

from code.Const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], bottom=position[1])

        # Physics
        self.current_frame = 0
        self.state = name
        self.frame_rate = 10  # Frames per second
        self.frame_duration = 1000 // self.frame_rate  # Duration of each frame in milliseconds
        self.animation_timer = 0  # Track time elapsed for the current frame

        self.last_update = pygame.time.get_ticks()
        self._gravity = 0
        self.is_grounded = True  # Track if the player is on the ground

        # Images and sounds
        self.animations = {
            "Enemy1": self._load_animation(f'./assets/{name}.png', frame_count=4),
            "Enemy2": self._load_animation(f'./assets/{name}.png', frame_count=12),
        }
        self.surf = self.animations[self.state][self.current_frame]  # Initial frame

    def _load_animation(self, path: str, frame_count: int):
        # Load a spritesheet and cut the frames
        spritesheet = pygame.image.load(path).convert_alpha()
        fliped_spritesheet = pygame.transform.flip(spritesheet, True, False)
        frame_width = fliped_spritesheet.get_width() // frame_count
        frame_height = fliped_spritesheet.get_height()
        frames = []
        for i in range(frame_count):
            frame = fliped_spritesheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            frames.append(frame)
        return frames

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

