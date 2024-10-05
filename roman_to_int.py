
#  covert the roman number to integer

def romanToInt(s):
	d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	value = 0
	for i in range(len(s)-1,-1,-1):
		   
		if (i+1)<len(s) and s[i] == 'I' and (s[i+1]=='V' or s[i+1]=='X') :
			value = value - d.get(s[i])
				
			    
		elif (i+1)<len(s) and s[i] == 'X' and (s[i+1]=='L' or s[i+1]=='C') :
			value = value - d.get(s[i])
				
			    
		elif (i+1)<len(s) and s[i] == 'C' and (s[i+1]=='D' or s[i+1]=='M') :
			value = value - d.get(s[i])
				
		else :
			value = value + d.get(s[i])
		       
                


	return value
        
print(romanToInt('XV'))
