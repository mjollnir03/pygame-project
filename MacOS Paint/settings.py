#Ellmaer Ranjber
import pygame as pg

pg.init()
pg.font.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
BROWN = (165,42,42)
PURPLE = (160, 32, 240)
ORANGE = (255,99,71)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)

FPS = 120

WIDTH, HEIGHT = 600, 750

ROWS = COLUMNS = 100

COLOR_BAR_HEIGHT = HEIGHT - WIDTH 

PIXEL_SIZE = (WIDTH // COLUMNS)

BG_COLOR = WHITE

DRAW_GRID_LINES = False

def get_font(size):
    return pg.font.SysFont("comic sans", size)