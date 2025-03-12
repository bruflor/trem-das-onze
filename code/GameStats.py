import sys
from datetime import datetime
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_ORANGE, COLOR_RED, COLOR_WHITE, COLOR_GREEN, SCORE_POS
from code.DBProxy import DBProxy


def get_formatted_date():
    """Returns the current date and time in a formatted string."""
    return datetime.now().strftime("%H:%M - %d/%m/%Y")


class GameStats:
    def __init__(self, name, window):
        self.window = window
        self.name = name
        self.surf = self._load_background_image()
        self.rect = self.surf.get_rect()
        self.font_cache = {}  # Cache for loaded fonts

    def _load_background_image(self):
        """Load and scale the background image."""
        image = pygame.image.load(f'./assets/{self.name}.png').convert_alpha()
        return pygame.transform.scale(image, (WIN_WIDTH, WIN_HEIGHT))

    def run(self, player_score=None):
        """Main loop for displaying game stats (Game Over, Game Win, Score, or Instructions screen)."""
        db_proxy = DBProxy('DBScore')
        self._play_background_music()

        waiting = True
        name = ''

        while waiting:
            self.window.blit(self.surf, self.rect)
            self._render_screen_content(player_score, name, db_proxy)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    waiting = self._handle_key_events(event, name, player_score, db_proxy)
                    if event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    elif len(name) < 4 and event.key != pygame.K_RETURN and event.key != pygame.K_ESCAPE:
                        name += event.unicode

            pygame.display.flip()

    def _play_background_music(self):
        """Load and play background music in a loop."""
        if self.name != 'Instructions':  # No music for the Instructions screen
            pygame.mixer_music.load(f'./assets/{self.name}.mp3')
            pygame.mixer_music.play(-1)
            pygame.mixer_music.set_volume(0.3)

    def _render_screen_content(self, player_score, name, db_proxy):
        """Render text and other content based on the screen type."""
        if self.name == 'GameOver':
            self._render_text(48, "GAME", COLOR_ORANGE, (WIN_WIDTH / 2, 70))
            self._render_text(92, "OVER", COLOR_RED, (WIN_WIDTH / 2, 120))
        elif self.name == 'GameWin':
            self._render_text(92, "YOU WIN", COLOR_GREEN, (WIN_WIDTH / 2, 50))
            self._render_text(36, "You came home safely!", COLOR_WHITE, (WIN_WIDTH / 2, 100))
            self._render_text(48, f'Score: {player_score}', COLOR_GREEN, (WIN_WIDTH / 2, 210))
            self._render_text(18, "Enter player name (4 character)", COLOR_WHITE, (WIN_WIDTH / 2, 230))
            self._render_text(18, "and press enter to save score:", COLOR_WHITE, (WIN_WIDTH / 2, 245))
            self._render_text(56, name, COLOR_WHITE, (WIN_WIDTH / 2, 140))
        elif self.name == 'Score':
            self._render_score_screen(db_proxy)
        elif self.name == 'Instructions':
            self._render_instructions_screen()

        self._render_text(16, "Press ESC button to return to menu", COLOR_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT - 30))

    def _render_score_screen(self, db_proxy):
        """Render the top 10 scores on the score screen."""
        self._render_text(48, 'TOP 10 SCORE', COLOR_GREEN, SCORE_POS['Title'])
        self._render_text(20, 'NAME     SCORE           DATE      ', COLOR_GREEN, SCORE_POS['Label'])

        list_score = db_proxy.retrieve_top10()
        for idx, player_score in enumerate(list_score):
            id_, name, score, date = player_score
            self._render_text(20, f'{name}     {score:05d}     {date}', COLOR_WHITE, SCORE_POS[idx])

    def _render_instructions_screen(self):
        """Render the Instructions screen with controls and story side by side, left-aligned."""
        self._render_text(48, 'INSTRUCTIONS', COLOR_GREEN, (WIN_WIDTH / 2, 50))
        self._render_text(14, 'developed By Bruna Flôr (RU 4596056)', COLOR_WHITE, (WIN_WIDTH/2, 80))
        # Left Column: Controls
        self._render_text_left(24, 'Controls:', COLOR_WHITE, (WIN_WIDTH / 4 - 100, 120))
        self._render_text_left(18, 'Move Left: LEFT ARROW', COLOR_WHITE, (WIN_WIDTH / 4 - 100, 150))
        self._render_text_left(18, 'Move Right: RIGHT ARROW', COLOR_WHITE, (WIN_WIDTH / 4 - 100, 170))
        self._render_text_left(18, 'Jump: SPACE or UP ARROW', COLOR_WHITE, (WIN_WIDTH / 4 - 100, 190))
        self._render_text_left(18, 'Attack: R-CONTROL', COLOR_WHITE, (WIN_WIDTH / 4 - 100, 210))

        # Right Column: Story
        self._render_text_left(24, 'Story:', COLOR_WHITE, (2.5 *WIN_WIDTH / 4 - 100, 120))
        self._render_text_left(18, 'You are a brave adventurer trying to', COLOR_WHITE, (2.5 *WIN_WIDTH / 4 - 100, 150))
        self._render_text_left(18, 'return home after a long day.', COLOR_WHITE, (2.5 *WIN_WIDTH / 4 - 100, 170))
        self._render_text_left(18, 'Fight enemies, avoid obstacles,', COLOR_WHITE, (2.5 *WIN_WIDTH / 4 - 100, 190))
        self._render_text_left(18, 'and make it back safely!', COLOR_WHITE, (2.5 *WIN_WIDTH / 4 - 100, 210))

    def _render_text_left(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        """Render text on the screen aligned to the left."""
        if text_size not in self.font_cache:
            self.font_cache[text_size] = pygame.font.Font('./assets/Jersey10-Regular.ttf', text_size)
        text_surf: Surface = self.font_cache[text_size].render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(topleft=text_pos)
        self.window.blit(text_surf, text_rect)

    def _handle_key_events(self, event, name, player_score, db_proxy):
        """Handle key events for input and navigation."""
        if event.key == pygame.K_RETURN and len(name) == 4:
            db_proxy.save({'name': name, 'score': player_score, 'date': get_formatted_date()})
            return False  # Exit the loop
        elif event.key == pygame.K_ESCAPE:
            return False  # Exit the loop
        return True  # Continue waiting

    def _render_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        """Render text on the screen using cached fonts."""
        if text_size not in self.font_cache:
            self.font_cache[text_size] = pygame.font.Font('./assets/Jersey10-Regular.ttf', text_size)
        text_surf: Surface = self.font_cache[text_size].render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)