
def initialize():
	print("Wel Come to the GAME")
	size = int(input("Enter the Grid size \n"))
	grid = [[" "]*size]*size
	return grid

def display(game_state):
	size = len(game_state)
	for i in range(1, size*2+2):
		if i%2:
			for k in range(size*2):
				print('_',end=' ')
			print()
		else:
			for j in range(size*2+1):
				if j%2:
					print('',end=' ')
				else:
					print('|',end='')
			print(end='\n')
		
	
			



def tic_tak_toe():
	game_state = initialize()
	
	display(game_state)
	
tic_tak_toe()
