from .piece import Piece
from ..settings import grid,pieces
king=[(i,j) for i in range(-1,2) for j in range(-1,2) if abs(i)+abs(j)>0]
class King(Piece):
    def __init__(self, square, isWhite):
        super().__init__(square, isWhite,'k')
        self.hasMoved=False
        self.inCheck=False
    def defineMovement(self, square):
        freedomPoints=[(square.ord+kg[0],square.abs+kg[1]) for kg in king if (square.ord+kg[0] in range(8) and square.abs+kg[1] in range(8))]
        freedom=[grid[coor[0]][coor[1]] for coor in freedomPoints]
        notfreedom=[sq for sq in freedom if (sq.piece and sq.piece.type[0]==self.type[0])]
        freedom=list(set(freedom)-set(notfreedom))
        for p in pieces:
            if p.type[1]!='k':
                p.freedom=p.defineMovement(p.square)
        stopped={sq for sq in [p.freedom for p in pieces] if sq in freedom}
        freedom=list(set(freedom)-stopped)
        return freedom
    def move(self,square):
        super().move(square)
        self.hasMoved=True