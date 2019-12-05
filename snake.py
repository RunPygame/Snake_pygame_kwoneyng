import pygame
import time
from datetime import datetime
from datetime import timedelta



SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
rect = pygame.Rect((0,0), (SCREEN_WIDTH, SCREEN_HEIGHT))

RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
PURPLE = 127, 0, 127
BLACK = 0, 0, 0
GRAY = 127, 127, 127
WHITE = 255, 255, 255 

# # time.sleep(4)
# pygame.draw.rect(screen, WHITE, rect)
# rect = pygame.Rect((0,0),(40,40))
# pygame.draw.rect(screen, GREEN, rect)

# rect = pygame.Rect((340,60), (60, 120))
# pygame.draw.rect(screen, RED, rect)

# pygame.display.update()
# SCREEN_WIDTH = 400
# SCREEN_HEIGHT = 400
# BLOCK_SIZE = 20

# def draw_background(screen):
#     background = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
#     pygame.draw.rect(screen, WHITE, background)

# def draw_block(screen, color, position):
#     block = pygame.Rect((position[1] * BLOCK_SIZE, position[0] * BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
#     pygame.draw.rect(screen, color, block)


# draw_background(screen)
# draw_block(screen, RED, (1, 1))
# draw_block(screen, RED, (3, 1))
# draw_block(screen, RED, (5, 1))
# draw_block(screen, RED, (7, 1))
# draw_block(screen, GREEN, (12, 10))
# draw_block(screen, GREEN, (12, 11))
# draw_block(screen, GREEN, (12, 12))
# draw_block(screen, GREEN, (12, 13))
# pygame.display.update()

# DIRECTION_ON_KEY = {
#     pygame.K_UP:'north',
#     pygame.K_DOWN:'south',
#     pygame.K_LEFT:'west',
#     pygame.K_RIGHT:'east',
# }

# block_direction = 'east'
# block_position = [0, 0]
# last_moved_time = datetime.now()

# while True:
#     events = pygame.event.get()
#     for event in events:
#         if event.type == pygame.QUIT:
#             exit()
#         if event.type == pygame.KEYDOWN:
#             if event.key in DIRECTION_ON_KEY:
#                 block_direction = DIRECTION_ON_KEY[event.key]

#     if timedelta(seconds=1) <= datetime.now() - last_moved_time:
#         # block_position[1] += 1
#         if block_direction == 'north':
#             block_position[0] -= 1
#         elif block_direction == 'south':
#             block_position[0] += 1
#         elif block_direction == 'west':
#             block_position[1] -= 1
#         elif block_direction == 'east':
#             block_position[1] += 1
#         last_moved_time = datetime.now()

#     draw_background(screen)
#     draw_block(screen, GREEN, block_position)
#     pygame.display.update()

class Snake:
    color = GREEN

    def __init__(self):
        self.positions = [(9,6), (9,7), (9,8), (9,9)]
        self.direction = 'north'

    def draw(self, screen):
        for position in self.positions:
            draw_block(screen, self.color, position)

class Apple:
    color = RED

    def __init__(self, position=(5,5)):
        self.position = position

    def draw(self, screen):
        draw_block(screen, self.color, self.position)

class GameBoard:
    width = 20
    height = 20

    def __init__(self):
        self.snake = Snake()
        self.apple = Apple()

    def draw(self, screen):
        self.apple.draw(screen)
        self.snake.draw(screen)

game_board = GameBoard()
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    draw_background(screen)
    game_board.draw(screen)
    pygame.display.update()
    