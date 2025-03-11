import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_ORANGE, COLOR_RED, COLOR_WHITE


class GameOver:
    def __init__(self, window):
        # adding a window
        self.window = window

        image = pygame.image.load('./assets/GameOver.png').convert_alpha()
        self.surf = pygame.transform.scale(image, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect()

        pygame.mixer_music.load('./assets/GameOver.mp3')
        # # Adding music in a loop with -1
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.5)

    def run(self):

        # Wait for user input to return to the menu
        waiting = True
        while waiting:
            # Display game over screen
            self.window.blit(self.surf, self.rect)
            self.screen_text(48, "GAME", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.screen_text(92, "OVER", COLOR_RED, ((WIN_WIDTH / 2), 120))
            self.screen_text(16, "Press any button to return to menu", COLOR_WHITE, ((WIN_WIDTH / 2), WIN_HEIGHT - 50))

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False  # Exit the game over screen and return to the menu

    # Adding method to create text
    def screen_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        font_path = './assets/Jersey10-Regular.ttf'
        text_font: Font = pygame.font.Font(font_path, text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)