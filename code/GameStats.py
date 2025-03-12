import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_ORANGE, COLOR_RED, COLOR_WHITE, COLOR_GREEN, SCORE_POS
from code.DBProxy import DBProxy


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%Y")
    return f"{current_time} - {current_date}"


class GameStats:
    def __init__(self, name, window):
        # adding a window
        self.window = window
        self.name = name

        image = pygame.image.load(f'./assets/{name}.png').convert_alpha()
        self.surf = pygame.transform.scale(image, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect()

    def run(self, player_score):
        db_proxy = DBProxy('DBScore')
        pygame.mixer_music.load(f'./assets/{self.name}.mp3')
        # # Adding music in a loop with -1
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.3)
        # Wait for user input to return to the menu
        waiting = True
        name = ''

        while waiting:
            # Display game over screen
            self.window.blit(self.surf, self.rect)
            if self.name == 'GameOver':
                self.screen_text(48, "GAME", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
                self.screen_text(92, "OVER", COLOR_RED, ((WIN_WIDTH / 2), 120))

            elif self.name == 'GameWin':
                self.screen_text(92, "YOU WIN", COLOR_GREEN, ((WIN_WIDTH / 2), 50))
                self.screen_text(36, "You came home safely!", COLOR_WHITE,
                                 ((WIN_WIDTH / 2), 100))

                self.screen_text(48, f'Score: {player_score}', COLOR_GREEN, ((WIN_WIDTH / 2), 210))
                self.screen_text(18, "Enter player name (4 character)", COLOR_WHITE,
                                 ((WIN_WIDTH / 2), 230))
                self.screen_text(18, "and press enter to save score:", COLOR_WHITE,
                                 ((WIN_WIDTH / 2), 245))
            elif self.name == 'Score':
                self.screen_text(48, 'TOP 10 SCORE', COLOR_GREEN, SCORE_POS['Title'])
                self.screen_text(20, 'NAME     SCORE           DATE      ', COLOR_GREEN, SCORE_POS['Label'])

                db_proxy = DBProxy('DBScore')
                list_score = db_proxy.retrieve_top10()
                db_proxy.close()

                for player_score in list_score:
                    id_, name, score, date = player_score
                    self.screen_text(20, f'{name}     {score:05d}     {date}', COLOR_WHITE,
                                    SCORE_POS[list_score.index(player_score)])

            self.screen_text(16, "Press ESC button to return to menu", COLOR_WHITE, ((WIN_WIDTH / 2), WIN_HEIGHT - 30))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': player_score, 'date': get_formatted_date()})
                        name=''
                        waiting = False
                    elif event.key == pygame.K_ESCAPE:
                        name = ''
                        waiting = False  # Exit the game over screen and return to the menu
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name +=event.unicode

            if self.name == 'GameWin':
                self.screen_text(56, name, COLOR_WHITE, ((WIN_WIDTH / 2), 140))
            pygame.display.flip()

    # Adding method to create text
    def screen_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        font_path = './assets/Jersey10-Regular.ttf'
        text_font: Font = pygame.font.Font(font_path, text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
