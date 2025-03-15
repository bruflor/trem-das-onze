import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT, PLAYER_MOV_RANGE, ENEMY_MOV_POS
from code.Enemy import Enemy
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
                for i in range(6):  # level 2 number of images
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case "Player":
                return Player('Player', (5, PLAYER_MOV_RANGE['ground']))
            case "Enemy1":
                return Enemy('Enemy1', (WIN_WIDTH + 10, ENEMY_MOV_POS['Enemy1']))
            case "Enemy2":
                return Enemy('Enemy2', (WIN_WIDTH + 10, ENEMY_MOV_POS['Enemy2']))
            case "Enemy3":
                return Enemy('Enemy3', (WIN_WIDTH + 10, ENEMY_MOV_POS['Enemy3']))
            case "Enemy4": # Pigeon
                return Enemy('Enemy4', (WIN_WIDTH + 10, ENEMY_MOV_POS['Enemy4']))
            case "Enemy5":
                return Enemy('Enemy5', (WIN_WIDTH + 10, ENEMY_MOV_POS['Enemy5']))
            case "Enemy6":
                return Enemy('Enemy6', (WIN_WIDTH + 10, ENEMY_MOV_POS['Enemy6']))
