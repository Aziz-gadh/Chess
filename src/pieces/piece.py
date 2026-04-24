import pygame as pg
from abc import abstractmethod,ABC
from ..settings import state

class Piece(pg.sprite.Sprite,ABC):
    def __init__(self,square,isWhite,type):
        super().__init__()
        self.type='w' if isWhite else 'b'
        self.type+=type
        self.image=pg.image.load('assets/images/pieces/'+self.type+'.png').convert_alpha()
        self.image=pg.transform.scale(self.image,square.rect.size)
        self.rect=square.rect
        self.square=square
        self.freedom=[]
        square.piece=self
    @abstractmethod
    def defineMovement(self,square):
        pass
    def select(self):
        self.freedom=self.defineMovement(self.square)
        for square in self.freedom:
            square.mark()
        self.selected=True
    def unselect(self):
        for square in self.freedom:
            square.unselect()
        self.selected=False
    def move(self,square):
        self.square.piece=None
        self.rect=square.rect
        self.square=square
        square.piece=self
        self.check()
    def check(self):
        global state
        self.freedom=self.defineMovement(self.square)
        for sq in self.freedom:
            if sq.piece and sq.piece.type[1]=='k' and sq.piece.type[0]==self.type[0]:
                state+=4
                sq.image.fill('#ff0011')
                sq.piece.inCheck=True
                break