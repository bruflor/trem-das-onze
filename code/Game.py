from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.GameStats import GameStats
from code.Level import Level
from code.Menu import Menu
import pygame
import sys

class Game:
    def __init__(self):
        # Start pygame
        pygame.init()
        pygame.display.set_caption("TREM-DAS-ONZE")

        # Set a window
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            # Show the menu
            menu = Menu(self.window)
            menu_return = menu.run()
            game_over = GameStats('GameOver',self.window)
            game_won = GameStats('GameWin',self.window)

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:  # Players
                player_score = [0, 0]  # [Player1, Player2]

                # Run Level 1
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)

                if level_return:
                    # Run Level 2 if Level 1 is completed
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)

                    if not level_return:
                        # Game over after Level 2
                        game_over.run(player_score[0])
                    else:
                        game_won.run(player_score[0])
                else:
                    # Game over after Level 1
                    game_over.run(player_score[0])

            elif menu_return == MENU_OPTION[3]:  # Score
                # Show score screen (placeholder)
                pass

            elif menu_return == MENU_OPTION[4]:  # Exit
                pygame.quit()
                sys.exit()

