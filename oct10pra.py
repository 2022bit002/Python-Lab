import random

def guess_game():
	ran_num = random.randint(1,10)
	guess = int(input("Enter the number between 1-10 and guess correctly\n"))
	if ran_num == guess:
		print("Correct guess :)")
	else:
		print("Incorrect Guess, Try again!!")
		
guess_game()
