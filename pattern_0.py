def draw_pattern(x):

	# the outer loop is for the nos. of rows
	# we have to connect it with the no. of rows to the the stars in the patter 
	# the inner loop is use to print inside it
	
	for i in range (x):
		for j in range (x):
			print('*',end=' ')
		print()

#draw_pattern(9)


def draw_pattern_0(x):
	for i in range(x):
		for j in range(i+1):
			print('*',end=' ')
		print()
	


def draw_pattern_1(x):
	for i in range(1,x+1):
		for j in range(i):
			print(j+1,end=' ')
			
		print()


def draw_pattern_2(x):
	for i in range(1,x+1):
		for j in range(i):
			print(i,end=' ')
			
		print()
	
def draw_pattern_3(x):
	for i in range(1,x+1):
		for j in range(x-i+1):
			print('*',end=' ')
		print()
		
def draw_pattern_4(x):
	for i in range(1,x+1):
		for j in range(x-i+1):
			print(j+1,end=' ')
		print()
		
		
		
		
def draw_pattern_5(x):
	for i in range(1,x+1):
		for j in range(x-i):
			print(' ',end='')
		for p in range(i):
			print('*',end='')
		for o in range(1,i):
			print('*',end='')
		print()

def draw_pattern_6(x):
	for i in range(1,x+1):
		for j in range(i):
			print(' ',end='')
		for p in range(2*x-(2*i+1)):
			print('*',end='')
		print()

def draw_pattern_7(x):
	for i in range(1,x+1):
		for j in range(x-i):
			print(' ',end='')
		for p in range(i):
			print('*',end='')
		for o in range(1,i):
			print('*',end='')
		print()
	for i in range(1,x+1):
		for j in range(i):
			print(' ',end='')
		for p in range(2*x-(2*i+1)):
			print('*',end='')
		print()
		
		
		
def draw_pattern_8(x):
	for i in range(2*x-1):
		for j in range(2*x-i):
			print('*',end='')
		print()

draw_pattern_8(5)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		

