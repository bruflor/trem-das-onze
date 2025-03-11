import random

import pygame
import sys

from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, EVENT_TIMEOUT, TIMEOUT_STEP, \
    TIMEOUT_LEVEL, WIN_WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
# from code.Enemy import Enemy


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode  # 1p, 2p cooperative or 2p competitive
        self.entity_list: list[Entity] = []

        # Getting all bg
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        # Adding the player
        player = EntityFactory.get_entity('Player')

        player.score = player_score[0]
        self.entity_list.append(player)

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)  # check victory condition

    def run(self, player_score):
        pygame.mixer_music.load(f'./assets/{self.name}.wav')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()  # FPS

        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, Player):
                    ent.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # if event.type == EVENT_ENEMY:
                #     choice = random.choice(('Enemy1', 'Enemy2'))
                #     self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        # updating score before timeout
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player':
                                player_score[0] = ent.score
                        return False

                # If we do not found any player because it was killed, return false to end game
                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True
                if not found_player:
                    return False
            # Texts
            self.level_text(14, f'{self.name} - Timeout {self.timeout / 1000 : .1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps() : .0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entities: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 25))
            pygame.display.flip()

            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        font_path = './assets/Jersey10-Regular.ttf'
        text_font: Font = pygame.font.Font(font_path, text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_surf, text_rect)
