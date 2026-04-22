import pygame as pg
from abc import abstractmethod,ABC

class Piece(pg.sprite.Sprite,ABC):
    def __init__(self,square,isWhite):
        super().__init__()
        self.rect=square.rect
        self.selected=False
        self.isWhite=isWhite
        self.freedom=self.defineMovement(square)
        square.piece=self
    @abstractmethod
    def defineMovement(self,square):
        pass
    def select(self):
        for square in self.freedom:
            square.mark()