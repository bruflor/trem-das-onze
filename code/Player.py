import pygame
from code.Const import ENTITY_SPEED, PLAYER_MOV_RANGE, WIN_WIDTH, WIN_HEIGHT, FRAME_COUNT, PLAYER_ATTACK_DELAY, \
    PLAYER_KEY_ATTACK
from code.Entity import Entity
from code.PlayerAttack import PlayerAttack


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        # Images and sounds
        self.animations = {
            "running": self._load_animation(f'./assets/{name}Run.png', frame_count=8),
            "running-backward": self._load_animation(f'./assets/{name}Run.png', frame_count=8, direction='backward'),
            "walking": self._load_animation(f'./assets/{name}Walk.png', frame_count=8),
            "jumping": self._load_animation(f'./assets/{name}Jump.png', frame_count=8),
            "attacking": self._load_animation(f'./assets/{name}Attack.png', frame_count=5),
        }
        self.jump_sound = pygame.mixer.Sound(f'./assets/Jump.wav')
        self.jump_sound.set_volume(0.3)

        self.attack_delay = PLAYER_ATTACK_DELAY

        self.last_update = pygame.time.get_ticks()
        self._gravity = 0
        self.is_grounded = True  # Track if the player is on the ground

    def update_animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 1000 // self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.animations[self.state])
            self.last_update = now
            self.surf = self.animations[self.state][self.current_frame]

    def apply_gravity(self):
        self._gravity += 1
        self.rect.y += self._gravity
        if self.rect.bottom >= PLAYER_MOV_RANGE['ground']:
            self.rect.bottom = PLAYER_MOV_RANGE['ground']
            self.is_grounded = True
            if self.state == "jumping":
                self.state = "walking"  # Reset to walking after landing
        else:
            self.is_grounded = False

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.is_grounded:
            self.state = "jumping"
            self._gravity = -15
            self.is_grounded = False
            self.jump_sound.play()
        elif keys[pygame.K_UP] and self.is_grounded:
            self.state = "jumping"
            self._gravity = -15
            self.is_grounded = False
            self.jump_sound.play()
        elif keys[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.x -= ENTITY_SPEED[self.name]
            self.state = "running-backward"
        elif keys[pygame.K_RIGHT] and self.rect.right <= PLAYER_MOV_RANGE['max_width']:
            self.rect.x += ENTITY_SPEED[self.name]
            self.state = "running"
        elif self.is_grounded:
            self.state = "walking"

    def attack(self):
        self.attack_delay -= 1
        if self.attack_delay == 0:
            self.attack_delay = PLAYER_ATTACK_DELAY
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_ATTACK[self.name]]:
                self.state = "attacking"
                return PlayerAttack(name=f'{self.name}Attack', position=(self.rect.centerx, self.rect.centery))
            else:
                return None
        else:
            return None

    def update(self):
        self.move()
        self.apply_gravity()
        self.update_animation()
