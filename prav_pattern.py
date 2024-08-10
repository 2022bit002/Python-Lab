# first question of pattern 

def print_patternQ1(x):
	a=x
	
	# first the above triangle of the pattern
	for i in range(x+1):
		for j in range(x+1-i):
			print(' ',end=" ")
		print('+',end=' ')
		if(i>0):
			for k in range(2*i-1):
				print(' ',end=' ')
			print('+',end =' ')
		
				
		print()
	
	
	# the lower trinagle of the pattern
	for q in range(x-1):
		for w in range(q+2):
			print(' ',end=' ')
		print('+',end=' ')
		for e in range(2*a+1-4):
			print(' ',end=' ')
		print('+',end=' ')
		a=a-1
		
		print()
		
	# the last sign of the pattern
	for r in range(1):
		for t in range(x+1):
			print(' ',end=' ')
		print('-')
	
		
# this triangle is similar to the one given above just have to replace the sign with another sign
def print_patternQ2(x):
	a=x
	
	# the above triangle of the pattern
	for i in range(x+1):
		for j in range(x+1-i):
			print(' ',end=" ")
		print('+',end=' ')
		if(i>0):
			for k in range(2*i-1):
				print(' ',end=' ')
			print('+',end =' ')
		
				
		print()
		
		
	# the lower triangle of the pattern 
	for q in range(x-1):
		for w in range(q+2):
			print(' ',end=' ')
		print('-',end=' ')
		for e in range(2*a+1-4):
			print(' ',end=' ')
		print('-',end=' ')
		a=a-1
		
		print()
	for r in range(1):
		for t in range(x+1):
			print(' ',end=' ')
		print('-')
	
		
		
		
print_patternQ1(3)
