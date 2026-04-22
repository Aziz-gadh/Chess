from .piece import Piece
from ..settings import grid
import pygame as pg

class Rook(Piece):
    def __init__(self,square,isWhite):
        super().__init__(square,isWhite,'r')
    def defineMovement(self,square):
        freedom=[]
        primary_hor=grid[square.ord]
        primary_ver=[ls[square.abs] for ls in grid]
        abs=square.abs+1
        while (abs<8 and not primary_hor[abs].piece):
            freedom.append(primary_hor[abs])
            abs+=1
        if abs!=8:
            freedom.append(primary_hor[abs])
        abs=square.abs-1
        while (abs>=0 and not primary_hor[abs].piece):
            freedom.append(primary_hor[abs])
            abs-=1
        if abs!=-1:
            freedom.append(primary_hor[abs])
        ord=square.ord+1
        while (ord<8 and not primary_ver[abs].piece):
            freedom.append(primary_ver[abs])
            ord+=1
        if ord!=8:
            freedom.append(primary_ver[ord])
        ord=square.ord-1
        while (ord>=0 and not primary_ver[abs].piece):
            freedom.append(primary_ver[abs])
            ord-=1
        if ord!=-1:
            freedom.append(primary_ver[ord])
        return freedom