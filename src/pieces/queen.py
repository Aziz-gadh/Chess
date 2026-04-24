from .bishop import Bishop
from .rook import Rook
from .piece import Piece

class Queen(Rook,Bishop):
    def __init__(self, square, isWhite):
        Piece.__init__(self,square, isWhite,'q')
        self.value=9
    def defineMovement(self, square):
        return Rook.defineMovement(self,square)+Bishop.defineMovement(self,square)