# Question to check wheather the string is valid or not it contains the parenthesis where it check if the parenthesis is properly closed.


def string_validation(text):
	length = len(text)
	check = ['(','[','<','{',')',']','>','}']
	result =[]
	if length == 0:
		return 0
	
	if  length%2!=0 or text[0] in check[4:]:
		return 0
		
	for i in text:
		if i not in check:
			return 0
	
	for i in text:
		if i in check[0:4]:
			result.append(i)
		else:
			if not result:
				return 0
			t = check.index(i)
			
			r = check.index(result.pop())
			if t - r != 4 :
				print(i,)
				return 0
	if result == []:
		return 1
	
	return 0
	
		
#print(string_validation(("<<<>>>")))



# return the count function of valid and invalid function

def valid_str(inpt):
	valid_count = 0
	invalid_count = 0
	
	for item in inpt:
	
		if isinstance(item,str):
			if string_validation(item):
				print(item)
				valid_count += 1
			else:
				invalid_count += 1
		elif isinstance(item,(list, tuple)):
			if valid_str(item):
				valid_count += 1
			else:
				invalid_count += 1
			#
	return (valid_count, invalid_count)
	
p = ['[](){}<>','sggs',('[[]]',''),23,'<>{}','{}}{',54,[23,53,74]]
print(valid_str(p))
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	



			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
	
