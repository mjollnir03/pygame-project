#Ellmaer Rnajber
from settings import *
from nav_bar import *
from sys import exit

WIN = pg.display.set_mode((WIDTH, HEIGHT)) 
pg.display.set_caption("MacOS Paint")

def init_grid(rows, columns, color):
    grid = []
    for i in range(rows):
        grid.append([])
        for _ in range(columns):
            grid[i].append(color)
    return grid

def draw(win, grid):
    win.fill(BG_COLOR)
    draw_grid(win, grid)
    for button in buttons:
        button.draw(win)
    pg.display.update() 

def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pg.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pg.draw.line(win, (0,0,0), (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))

        for i in range(COLUMNS + 1):
            pg.draw.line(win, (0,0,0), (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, HEIGHT - COLOR_BAR_HEIGHT))
    
def get_row_column_from_pos(pos):
    x,y = pos
    row = y // PIXEL_SIZE
    column = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError
    
    return row, column

clock = pg.time.Clock()
run = True
grid = init_grid(ROWS, COLUMNS, BG_COLOR)
drawing_color = BLACK
button_y = HEIGHT - COLOR_BAR_HEIGHT/2 - 15
buttons = [
        Button(5, button_y, 50, 50, BLACK),
        Button(65, button_y, 50, 50, BROWN),
        Button(125, button_y, 50, 50, RED),
        Button(185, button_y, 50, 50, PURPLE),
        Button(245, button_y, 50, 50, BLUE),
        Button(305, button_y, 50, 50, GREEN),
        Button(365, button_y, 50, 50, ORANGE),
        Button(425, button_y, 50, 50, YELLOW),
        Button(485, button_y, 50, 50, WHITE, "Erase"),
        Button(545, button_y, 50, 50, WHITE, "Clear")
    ]

while run:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    if pg.mouse.get_pressed()[0]:
        pos = pg.mouse.get_pos()
        try: 
            row, column = get_row_column_from_pos(pos)
            grid[row][column] = drawing_color
        except IndexError:
            for button in buttons:
                if not button.clicked(pos):
                    continue
                drawing_color = button.color
                if(button.text == "Clear"):
                    grid = init_grid(ROWS, COLUMNS, BG_COLOR)
                    drawing_color = BLACK

    draw(WIN, grid)

pg.quit()
exit()

