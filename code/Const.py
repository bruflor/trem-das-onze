import pygame

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (200, 212, 93)
COLOR_ORANGE = (219, 164, 99)
COLOR_RED = (173, 47, 79)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

PLAYER_MOV_RANGE = {
    'max_height': WIN_HEIGHT,
    'max_width': WIN_WIDTH + 470,
    'ground': WIN_HEIGHT - 30,
}

ENEMY_MOV_POS = {
    'Enemy1': WIN_HEIGHT - 60,
    'Enemy2': WIN_HEIGHT - 120,
}

PLAYER_FRAME_COUNT = {
    "idle": 5,
    "running": 8,
    "running-backward": 8,
    "walking": 8,
    "jumping": 8,
    "attacking": 5,
    "dead": 5,
}

ENEMY_FRAME_COUNT = {
    'Enemy1': 4,
    'Enemy2': 12,
}

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 0.3,
    'Level1Bg2': 0.6,
    'Level1Bg3': 0.9,
    'Level1Bg4': 1.2,
    'Level1Bg5': 1.6,
    'Level1Bg6': 2,
    'Level2Bg0': 0,
    'Level2Bg1': 0.5,
    'Level2Bg2': 1,
    'Level2Bg3': 1.5,
    'Level2Bg4': 2,
    'Level2Bg5': 2.5,
    'Player': 3,
    'PlayerAttack': 1,
    'Enemy1': 1,
    'Enemy2': 1,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Player': 300,
    'PlayerAttack': 1,
    'Enemy1': 50,
    'Enemy2': 80,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player': 1,
    'PlayerAttack': 25,
    'Enemy1': 10,
    'Enemy2': 20,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player': 0,
    'PlayerAttack': 0,
    'Enemy1': 100,
    'Enemy2': 125,
}

ENTITY_SHOT_DELAY = {
    'Player': 20,
    'Enemy1': 100,
    'Enemy2': 200,
}

# M
MENU_OPTION = ('NEW GAME - NORMAL',
               'NEW GAME - HARDCORE',
               'SCORE',
               'INSTRUCTIONS',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player': pygame.K_RIGHT}
PLAYER_KEY_ATTACK = {'Player': pygame.K_RCTRL}
PLAYER_KEY_JUMP = {'Player': pygame.K_SPACE}
PLAYER_KEY_RUN = {'Player': pygame.KMOD_SHIFT}

# S
SPAWN_TIME = 4000

# T
TIMEOUT_STEP = 100  # 100ms
TIMEOUT_LEVEL = 20000  # 20s

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }
