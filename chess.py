import pygame as pg
from square import Square
from settings import board_side,FPS,board,margin,side
pg.init()
running=True
clock=pg.time.Clock()
pg.display.set_caption('CHESS')
screen=pg.display.set_mode((board_side+margin[0]*2,board_side+margin[1]*2))
selectSquare=None
grid=[]
for i in range(8):
    grid.append([])
    for j in range(8):
        grid[i].append(Square(i,chr(j+ord('a'))))
        board.add(grid[i][j])
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        elif event.type==pg.MOUSEBUTTONDOWN:
            if selectSquare:
                selectSquare.selected=False
            mouse_position=[(pg.mouse.get_pos()[0]-margin[0])//side,(pg.mouse.get_pos()[1]-margin[1])//side]
            if mouse_position[0] in range(8) and mouse_position[1] in range(8):
                selectSquare=grid[mouse_position[0]][mouse_position[1]]
            if selectSquare:
                selectSquare.selected=True
    board.update()
    board.draw(screen)
    pg.display.update()
    clock.tick(FPS)
pg.quit()