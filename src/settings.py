import pygame as pg

side=80
board_side=side*8
FPS=60
board=pg.sprite.Group()
pieces=pg.sprite.Group()
black_square_color='#769656'
black_square_color_selected='#B9CA43'
white_square_color='#EEEED2'
white_square_color_selected='#F5F682'
margin=(40,80)
grid=[]
openMnt=[]
selectedPiece=None
state=0
score=0
# state=0b11234
# 1: 00 plying | 01 white wins | 10 black wins | 11 draw 
# 2: 0 no check | 1 check
# 3: 0 didn't select | 1 selected
# 4: 0 white to play | 1 black to play
horsee=[(i,j) for i in range(-2,3) for j in range(-2,3) if (i*j and abs(i)+abs(j)==3)]