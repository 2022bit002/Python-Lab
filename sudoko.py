import random

def initialize():
	sudoko_state = fill()
	#sudoko_state = {row : {col : ' ' for col in range(1, size+1)} for row in range(1, size+1)}
	#print(game_state)
	#for i in range(len(sudoko_state)):
	#	sudoko_state[i][i]=i+1
	
	display(sudoko_state)
	
def fill():	
	print('Wel-Come')
	size = int(input("Enter the grid size of the Sudoko\n"))
	sudoko_state = [list(" ")*size for _ in range(size)]
	posb = { i for i in range(1,size+1)}
	for row in range(size):	
		for col in range(size):
			avbl = set(sudoko_state[row] + [tr[col] for tr in sudoko_state] )
			print(avbl)
			c = list(posb - avbl)
			sudoko_state[row][col] = c.pop(random.randint(0,len(c)-1)) 
	return sudoko_state


def display(sudoko_state):
	size = len(sudoko_state)
	st = ' {} |'*size
	for row in range(size):
		print(' ---'*size)
		print('|',end='')
		#for col in range(size):
		#	print(f' {sudoko_state[row][col]} |',end='')
		#print('  |'.join(sudoko_state[row]),' |',end = ' ')
		print(st.format(*sudoko_state[row]))
		#print()
	print(' ---'*size)
def sudoko():
	initialize()
	#start_game()
	#end_game()


sudoko()


