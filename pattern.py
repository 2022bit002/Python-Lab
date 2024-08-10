

def print_pattern(x):
	
	a=x
	
	# The upper part of the pattern:
	for i in range(x+1):
		for j in range(x+1-i): 
			print(" ",end=' ')
		print('*',end=' ')
		
		if(i>0):	
			for k in range(2*i-1):
				if(i==x):
					if(k==x-1):
						print(x ,end=' ')
					else:
						print(' ',end=' ')
				else:
					print(' ',end=' ')
				
			print('*',end =' ')
		print()
		
	
	
	# The lower pyramid of the pattern	
	for q in range(x-1):
		for w in range(q+2):
			print(' ', end=' ')
		print('*',end=' ')
		for e in range(2*a-3):
			print(' ',end=' ')
		print('*',end=' ')
		a=a-1
		print()
	
	# The block at last of the pattern.
	for r in range (x):
		for t in range(2*x+3):
			print('*',end=' ')
		print()
		
	


print_pattern(5) 


