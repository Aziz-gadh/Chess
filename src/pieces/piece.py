import pygame as pg
from abc import abstractmethod,ABC

class Piece(pg.sprite.Sprite,ABC):
    def __init__(self,square,isWhite,type):
        super().__init__()
        self.type='w' if isWhite else 'b'
        self.type+=type
        self.image=pg.image.load('assets/images/'+self.type+'.png').convert_alpha()
        self.image=pg.transform.scale(self.image,square.rect.size)
        self.rect=square.rect
        self.selected=False
        self.freedom=self.defineMovement(square)
        square.piece=self
    @abstractmethod
    def defineMovement(self,square):
        pass
    def select(self):
        for square in self.freedom:
            square.mark()