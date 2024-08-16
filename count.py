
def count_substring(x,y):
	
	count = -1
	
	for i in x:
		if(i==y):
			if(count == -1):
				count =1
			else:
				count += 1
	
	
	return count;  





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







print(count_overlaping('pannnkajnnnmnnnnkaahafdhkkjjgh','nn',False))
