from .piece import Piece
from ..settings import grid
horsee=[(i,j) for i in range(-2,3) for j in range(-2,3) if (i*j and abs(i)+abs(j)==3)]
class Knight(Piece):
    def __init__(self,square,isWhite):
        super().__init__(square,isWhite,'n')
        self.value=3
    def defineMovement(self, square):
        freedomPoints=[(square.ord+horsy[0],square.abs+horsy[1]) for horsy in horsee if (square.ord+horsy[0] in range(8) and square.abs+horsy[1] in range(8))]
        freedom=[grid[coor[0]][coor[1]] for coor in freedomPoints]
        notfreedom=[sq for sq in freedom if (sq.piece and sq.piece.type[0]==self.type[0])]
        return [sq for sq in freedom if sq not in notfreedom]