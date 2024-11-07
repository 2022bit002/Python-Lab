import random 

def initialization():
	
	
	return random.randint(1,200), [5,4,3,2,1] 

def start_game(num):
	ran_num , reward = num
	amount = int(input("Enter the Entry fees for the game and win atmost you can"))
	for i in range(1,6):
		print("Attempt "+i)
		guess = int(input("Enter your guess"))
		
		if guess == ran_num:
			print(reward[i-1]*amount)
		else:
			if guess > ran_num:
				g = (guess-ran_num)//guess
				if g < 0.5:
					print("large number")  
				else:
					print("too large number")
			else:
				g = (ran_num - guess)//ran_num
				if g < 0.5:
					print("too small number")
				else:
					print("small number")
		

def guess_and_win_game():
	game_state = initialization()
	start_game(game_state)
	
	
	
