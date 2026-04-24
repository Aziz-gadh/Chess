import pygame as pg
from .square import Square
from .settings import board_side,FPS,board,margin,side,grid,pieces,state
from .pieces.rook import Rook
from .pieces.bishop import Bishop
from .pieces.queen import Queen
from .pieces.knight import Knight
pg.init()
running=True
clock=pg.time.Clock()
pg.display.set_caption('CHESS')
screen=pg.display.set_mode((board_side+margin[0]*2,board_side+margin[1]*2))
selectSquare=None
for i in range(8):
    grid.append([])
    for j in range(8):
        grid[i].append(Square(i,chr(j+ord('a'))))
        board.add(grid[i][j])
pieces.add(Rook(grid[0][0],False))
pieces.add(Rook(grid[0][7],True))
pieces.add(Rook(grid[7][0],False))
pieces.add(Rook(grid[7][7],True))
pieces.add(Bishop(grid[2][0],False))
pieces.add(Bishop(grid[5][0],False))
pieces.add(Bishop(grid[2][7],True))
pieces.add(Bishop(grid[5][7],True))
pieces.add(Knight(grid[1][0],False))
pieces.add(Knight(grid[1][7],True))
pieces.add(Knight(grid[6][0],False))
pieces.add(Knight(grid[6][7],True))
pieces.add(Queen(grid[3][7],True))
pieces.add(Queen(grid[3][0],False))
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        elif event.type==pg.MOUSEBUTTONDOWN:
            if selectSquare:
                selectSquare.unselect()
                selectSquare.unmark()
            mouse_position=[(pg.mouse.get_pos()[0]-margin[0])//side,(pg.mouse.get_pos()[1]-margin[1])//side]
            if selectSquare==grid[mouse_position[0]][mouse_position[1]]:
                    selectSquare=None
                    if state & 2:
                        state-=2
            else:
                if mouse_position[0] in range(8) and mouse_position[1] in range(8) and not (state>>5):
                    selectSquare=grid[mouse_position[0]][mouse_position[1]]
                else:
                    selectSquare=None
                if selectSquare:
                    selectSquare.select()
    board.draw(screen)
    pieces.draw(screen)
    pg.display.update()
    clock.tick(FPS)
pg.quit()