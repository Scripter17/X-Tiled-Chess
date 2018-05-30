import ChessMoves, pygame, sys
pygame.init()
size=(576, 576)
screen=pygame.display.set_mode(size)
board=defBoard=[
	[[0,1,False], [0,2,False], [0,3,False], [0,4,False], [0,5,False], [0,3,False], [0,2,False], [0,1,False]],
	[[0,6,False], [0,6,False], [0,6,False], [0,6,False], [0,6,False], [0,6,False], [0,6,False], [0,6,False]],
	[[0,0,False], [0,0,False], [0,0,False], [0,0,False], [0,0,False], [0,0,False], [0,0,False], [0,0,False]],
	[[0,0,False], [0,0,False], [0,0,False], [0,0,False], [0,0,False], [0,0,False], [0,0,False], [0,0,False]],
	[[1,0,False], [1,0,False], [1,0,False], [1,0,False], [1,0,False], [1,0,False], [1,0,False], [1,0,False]],
	[[1,0,False], [1,0,False], [1,0,False], [1,0,False], [1,0,False], [1,0,False], [1,0,False], [1,0,False]],
	[[1,6,False], [1,6,False], [1,6,False], [1,6,False], [1,6,False], [1,6,False], [1,6,False], [1,6,False]],
	[[1,1,False], [1,2,False], [1,3,False], [1,4,False], [1,5,False], [1,3,False], [1,2,False], [1,1,False]]
]
player=1
pieces=[" ♜♞♝♛♚♟", " ♖♘♗♕♔♙"]
fnt=pygame.font.Font("arialuni.ttf", 64)
def WaitForMouse():
	while not pygame.mouse.get_pressed()[0]:
		for e in pygame.event.get():
			if e.type==pygame.QUIT:
				sys.exit()
	return pygame.mouse.get_pos()

while True:
	screen.fill((255,255,255))
	for y in range(8):
		for x in range(8):
			if (x^y)%2:
				pygame.draw.rect(screen, (192,192,192), [x*64+64, y*64, 64, 64])
			screen.blit(fnt.render(pieces[board[y][x][0]][board[y][x][1]], False, (0, 0, 0)), (x*64+64, y*64-16))
		screen.blit(fnt.render("87654321"[y], False, (0, 0, 0)), (0, y*64-16))
		screen.blit(fnt.render("ABCDEFGH"[y], False, (0, 0, 0)), (y*64+64, 496))
	pygame.display.flip()
	c=WaitForMouse()
	while pygame.mouse.get_pressed()[0]:
		pygame.event.get()
	c=((c[0]-64)//64, c[1]//64)
	if board[c[1]][c[0]][0]==player:
		moves=ChessMoves.funcs[board[c[1]][c[0]][1]](c, board)
		if moves!=[]:
			for n in moves:
				pygame.draw.rect(screen, (255,255,0), [n[0]*64+64, n[1]*64, 64, 64])
				screen.blit(fnt.render(pieces[board[n[1]][n[0]][0]][board[n[1]][n[0]][1]], False, (0, 0, 0)), (n[0]*64+64, n[1]*64-16))
			pygame.draw.rect(screen, (119,119,0), [c[0]*64+64, c[1]*64, 64, 64])
			screen.blit(fnt.render(pieces[board[c[1]][c[0]][0]][board[c[1]][c[0]][1]], False, (0, 0, 0)), (c[0]*64+64, c[1]*64-16))
			pygame.display.flip()
			c2=WaitForMouse()
			while pygame.mouse.get_pressed()[0]:
				pygame.event.get()
			c2=((c2[0]-64)//64, c2[1]//64)
			while c2 not in [*moves, c]:
				c2=WaitForMouse()
				while pygame.mouse.get_pressed()[0]:
					pygame.event.get()
				c2=((c2[0]-64)//64, c2[1]//64)
			if c==c2:
				pass
			elif c2 in moves:
				board[c2[1]][c2[0]]=board[c[1]][c[0]]
				board[c[1]][c[0]]=[1-player,0,True]
				board[c2[1]][c2[0]][2]=True
				board[c[1]][c[0]][2]=True
				player^=1
