from .piece import Piece
from ..settings import grid
import pygame as pg

class Rook(Piece):
    def __init__(self,square,isWhite):
        super().__init__(square,isWhite,'r')
        self.value=5
    def defineMovement(self,square):
        freedom=[]
        primary_hor=grid[square.ord]
        primary_ver=[ls[square.abs] for ls in grid]
        for abs in range(square.abs+1,8):
            freedom.append(primary_hor[abs])
            if freedom[-1].piece and freedom[-1].piece.type[0]!=self.type[0]:
                break
            elif freedom[-1].piece and freedom[-1].piece.type[0]==self.type[0]:
                freedom.pop()
                break
        for abs in range(square.abs-1,-1,-1):
            freedom.append(primary_hor[abs])
            if freedom[-1].piece and freedom[-1].piece.type[0]!=self.type[0]:
                break
            elif freedom[-1].piece and freedom[-1].piece.type[0]==self.type[0]:
                freedom.pop()
                break
        for ord in range(square.ord+1,8):
            freedom.append(primary_ver[ord])
            if freedom[-1].piece and freedom[-1].piece.type[0]!=self.type[0]:
                break
            elif freedom[-1].piece and freedom[-1].piece.type[0]==self.type[0]:
                freedom.pop()
                break
        for ord in range(square.ord-1,-1,-1):
            freedom.append(primary_ver[ord])
            if freedom[-1].piece and freedom[-1].piece.type[0]!=self.type[0]:
                break
            elif freedom[-1].piece and freedom[-1].piece.type[0]==self.type[0]:
                freedom.pop()
                break
        return freedom