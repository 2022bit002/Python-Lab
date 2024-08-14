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
	
		
# The modulo function and its implementation

def modulo_fun(numerator,denominator):

	quoient = numerator // denominator 
	remainder = numerator - (quoient * denominator)
	return remainder	
		


#  count function and itss implementation

def count_overlaping(x,y,z):
	
	length = len(x)
	count = -1
	if(z==True):
		for i in range(len(x)):
			if(x[i] == y[0]):
				j,m=i,0
				for q in range(len(y)):	
					if (j < length and x[j] == y[q] ):
						m,j=m+1,j+1
					else: 
						break
				if(m==len(y)):
					if(count == -1):
						count = 1	
					else:
						count +=1
		return count;
	
	else:
		i = 0
		while (i <= length - len(y)):
		    if (x[i] == y[0]):
		        j = i
		        m = 0
		        for q in range(len(y)):
		            if (j < length and x[j] == y[q]):  
		                m += 1
		                j += 1
		            else:
		                break  
		        if m == len(y):  
		            if count == -1:
		                count = 1
		            else:
		                count += 1
		            i = j  
		        else:
		            i += 1
		    else:
		        i += 1
		return count







#print(count_overlaping('pannnkajnnnmnnnnkaahafdhkkjjgh','nn',False))

