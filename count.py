
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
	
	
	count = -1
	if(z==False):
		for i in range(len(x)):
			if(x[i]==y[0]):
			
				j=i
				m=-1
				for q in range(len(y)):
					#print(x[j])
					#print(y[q])
					
					if (x[j]==y[q]):
						#print(x[j],y[q])
						m+=1
						j+=1
						#print(m,q)
				if(m==q):
					if(count == -1):
						count = 1	
					else:
						count +=1
	return count;








print(count_overlaping('pankajpankajkajpannkjkaj','a',False))
