from .piece import Piece
from ..settings import side,grid
import pygame as pg

class Rook(Piece):
    def __init__(self,square,isWhite):
        self.type='wr' if isWhite else 'br'
        self.image=pg.image.load('assets/images/'+self.type+'.png').convert_alpha()
        self.image=pg.transform.scale(self.image,square.rect.size)
        super().__init__(square,isWhite)
    def defineMovement(self,square):
        freedom=[]
        primary_hor=grid[square.ord]
        primary_ver=[ls[square.abs] for ls in grid]
        abs=square.abs
        while (abs<8 and not primary_hor[abs].piece):
            freedom.append(primary_hor[abs])
            abs+=1
        if abs!=8:
            freedom.append(primary_hor[abs])
        abs=square.abs
        while (abs>=0 and not primary_hor[abs].piece):
            freedom.append(primary_hor[abs])
            abs-=1
        if abs!=-1:
            freedom.append(primary_hor[abs])
        ord=square.ord
        while (ord<8 and not primary_ver[abs].piece):
            freedom.append(primary_ver[abs])
            ord+=1
        if ord!=8:
            freedom.append(primary_ver[ord])
        ord=square.ord
        while (ord>=0 and not primary_ver[abs].piece):
            freedom.append(primary_ver[abs])
            ord-=1
        if ord!=-1:
            freedom.append(primary_ver[ord])
        return freedom