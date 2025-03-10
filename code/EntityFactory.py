import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player

# Design pattern Factory
class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case "Level1Bg":
                list_bg = []
                for i in range(7):  # level 1 number of images
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case "Level2Bg":
                list_bg = []
                for i in range(5):  # level 2 number of images
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case "Player":
                return Player('Player', (10, WIN_HEIGHT / 2 - 30))
            case "Enemy1":
                pass
                # return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(10, WIN_HEIGHT - 40)))
