def str_to_int(text):
	text = text.lstrip('0')
	ok=text.isdigit()
	p ={49:1, 50:2, 51:3, 52:4, 53:5, 54:6 ,55:7, 56:8, 57:9, 48:0}
	length = len(text)
	num,n = 0,length-1
	if length == 0:
		return 0
	for i in range(length):
		if ok:
			o = ord(text[i])
			l = p.get(o)
			
			num = l*pow(10,n) + num
			n-=1
			
		else:
			return "Invalid Input" 
	return num		
	
	
	
	
#print(str_to_int('16456'))


















