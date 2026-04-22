import pygame as pg
from .settings import side,black_square_color,white_square_color,margin,white_square_color_selected,black_square_color_selected
class Square(pg.sprite.Sprite):
    def __init__(self,n,a):
        super().__init__()
        self.ord=n
        self.letter=a
        self.abs=ord(a)-ord('a')
        self.isBlack=(self.ord+self.abs)%2
        self.color=black_square_color if (self.ord+self.abs)%2 else white_square_color
        self.image=pg.Surface((side,side),pg.SRCALPHA)
        self.rect=self.image.get_rect(topleft=(self.ord*side+margin[0],self.abs*side+margin[1]))
        self.selected=False
        self.piece=None
    def mark(self):
        if self.piece:
            pg.draw.rect(self.image,(240,20,80,100),(0,0,side,side),20)
        else:
            pg.draw.circle(self.image,(0,0,0,100),(side//2,side//2),side//2)
    def update(self):
        if self.selected:
            if self.isBlack:
                self.image.fill(black_square_color_selected)
            else:
                self.image.fill(white_square_color_selected)
        else:
            self.image.fill(self.color)
#Change this awful mechenic!!!!!!!!!!