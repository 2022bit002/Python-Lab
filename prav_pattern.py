def print_pattern(x):
	for i in range(x+1):
		for j in range(x+1-i):
			print(' ',end=" ")
		print('+',end=' ')
		if(i>0):
			for k in range(2*i-1):
				print(' ',end=' ')
			print('+',end =' ')
		
				
		print()
		
	for q in range(x-1):
		for w in range(q+2):
			print(' ',end=' ')
		print('+',end=' ')
		print()
	
		
		
		
		
print_pattern(5)
