# 0-Blank, 1-Rook, 2-Knight, 3-Bishop, 4-Queen, 5-King, 6-Pawn
# p-Point, m-Moved, b-Board
def rook(p, b):
	x,y=p
	r=[]
	for d in [7,1]:
		for l in range(1,8,1):
			if b[y][(x+d*l)%8][1]!=0: # If a piece is found, stop looking
				if b[y][(x+d*l)%8][0]!=b[y][x][0]: # If the piece found is not the current player's color, add it to the destination list
					r.append(((x+d*l)%8, y))
				break
			r.append(((x+d*l)%8, y))
	
	for d in [-1,1]:
		for l in range(1,8,1):
			if not (0<=y+d*l<=7): # If destination would be off of the board, just skip it
				break
			if b[y+d*l][x][1]!=0:
				if b[y+d*l][x][0]!=b[y][x][0]:
					r.append((x, y+d*l))
				break
			r.append((x, y+d*l))
	return r

def knight(p, b):
	x,y=p
	r=[]
	for d in [(1,-2), (2,-1), (2,1), (1,2), (7,2), (6,1), (6,-1), (7,-2)]:
		if not (0<=y+d[1]<=7):
			continue
		if b[y+d[1]][(x+d[0])%8][0]!=b[y][x][0] or b[y+d[1]][(x+d[0])%8][1]==0:
			r.append(((x+d[0])%8, y+d[1]))
	return r

def bishop(p, b):
	x,y=p
	r=[]
	for d in [(1,-1), (1,1), (7,1), (7,-1)]:
		for l in range(1,8,1):
			if not (0<=y+d[1]*l<=7):
				break
			if b[y+d[1]*l][(x+d[0]*l)%8][1]!=0:
				if b[y+d[1]*l][(x+d[0]*l)%8][0]!=b[y][x][0]:
					r.append(((x+d[0]*l)%8, y+d[1]*l))
				break
			r.append(((x+d[0]*l)%8, y+d[1]*l))
	return r

def queen(p, b):
	r=[]
	r.append(bishop(p, b))
	r.append(rook(p, b))
	r=[*r[0], *r[1]]
	return r

def king(p, b): # TODO: ADD CASTLING
	x,y=p
	r=[]
	for d in [(0,-1), (1,-1), (1,0), (1,1), (0,1), (7,1), (7,0), (7,-1)]:
		if not (0<=y+d[1]<=7):
			continue
		if b[y+d[1]][(x+d[0])%8][0]!=b[y][x][0] or b[y+d[1]][(x+d[0])%8][1]==0:
			r.append(((x+d[0])%8, y+d[1]))
	return r

def pawn(p, b):
	x,y=p
	r=[]
	s=(-1 if b[y][x][0]==1 else 1)
	if 0<=y+s<=8 and b[y+s][x][1]==0: # Go forward
		r.append((x,y+s))
		if 0<=y+s*2<=8 and b[y+s*2][x][1]==0 and b[y][x][2]==False: # Move 2 tiles if the pawn wasn't moved
			r.append((x,y+s*2))
	if 0<=y+s<=8 and b[y+s][(x+1)%8][0]!=b[y][x][0] and b[y+s][(x+1)%8][1]!=0: # Attact right
		r.append(((x+1)%8, y+s))
	if 0<=y+s<=8 and b[y+s][(x+7)%8][0]!=b[y][x][0] and b[y+s][(x+7)%8][1]!=0: # Attact left
		r.append(((x+7)%8, y+s))
	return r

funcs=[(lambda p,b:[]), rook, knight, bishop, queen, king, pawn]