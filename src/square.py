import pygame as pg
from .settings import side,black_square_color,white_square_color,margin,white_square_color_selected,black_square_color_selected
class Square(pg.sprite.Sprite):
    def __init__(self,n,a):
        super().__init__()
        self.ord=n
        self.letter=a
        self.abs=ord(a)-ord('a')
        self.isBlack=(self.ord+self.abs)%2
        self.color=black_square_color if self.isBlack else white_square_color
        self.image=pg.Surface((side,side),pg.SRCALPHA)
        self.image.fill(self.color)
        self.rect=self.image.get_rect(topleft=(self.ord*side+margin[0],self.abs*side+margin[1]))
        self.colorSelect=black_square_color_selected if self.isBlack else white_square_color_selected
        self.piece=None
    def mark(self):
        overlay = pg.Surface((side, side), pg.SRCALPHA)  # fresh transparent surface
        if self.piece:
            pg.draw.circle(overlay, (0, 0, 0, 83), (side//2, side//2), side*3//8, 5)
        else:
            pg.draw.circle(overlay, (0, 0, 0, 83), (side//2, side//2), side//4)
        self.image.blit(overlay, (0, 0))
    def select(self):
        self.image.fill(self.colorSelect)
        if self.piece:
            self.piece.select()
    def unselect(self):
        self.image.fill(self.color)
    def unmark(self):
        if self.piece:
            self.piece.unselect()