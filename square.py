import pygame as pg
from settings import side,black_square_color,white_square_color,margin
class Square(pg.sprite.Sprite):
    def __init__(self,n,a):
        super().__init__()
        self.abs=n
        self.letter=a
        self.ord=ord(a)-ord('a')
        self.isBlack=(self.abs+self.ord)%2
        self.color=black_square_color if (self.abs+self.ord)%2 else white_square_color
        self.image=pg.Surface((side,side),pg.SRCALPHA)
        self.rect=self.image.get_rect(topleft=(self.abs*side+margin[0],self.ord*side+margin[1]))
        self.selected=False
    def update(self):
        if self.selected:
            if self.isBlack:
                self.image.fill('#B9CA43')
            else:
                self.image.fill('#F5F682')
        else:
            self.image.fill(self.color)