from .piece import Piece
from ..settings import grid

class Bishop(Piece):
    def __init__(self,square,isWhite):
        super().__init__(square,isWhite,'b')
        self.value=3
    def defineMovement(self,square):
        freedom=[]
        j,i=square.abs+1,square.ord+1
        while(i<8 and j<8 and not grid[i][j].piece):
            freedom.append(grid[i][j])
            i+=1
            j+=1
        if i!=8 and j!=8 and grid[i][j].piece.type[0]!=self.type[0]:
            freedom.append(grid[i][j])
        j,i=square.abs+1,square.ord-1
        while(j<8 and i>-1 and not grid[i][j].piece):
            freedom.append(grid[i][j])
            j+=1
            i-=1
        if j!=8 and i!=-1 and grid[i][j].piece.type[0]!=self.type[0]:
            freedom.append(grid[i][j])
        j,i=square.abs-1,square.ord+1
        while(j>-1 and i<8 and not grid[i][j].piece):
            freedom.append(grid[i][j])
            j-=1
            i+=1
        if j!=-1 and i!=8 and grid[i][j].piece.type[0]!=self.type[0]:
            freedom.append(grid[i][j])
        j,i=square.abs-1,square.ord-1
        while(i>-1 and j>-1 and not grid[i][j].piece):
            freedom.append(grid[i][j])
            i-=1
            j-=1
        if i!=-1 and j!=-1 and grid[i][j].piece.type[0]!=self.type[0]:
            freedom.append(grid[i][j])
        return freedom