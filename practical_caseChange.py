# Practical of 15/08 4 functions that will convet a string into small case , capital case , reverse string , zig zag pattern


# Convert the string into samll case
def small_case(text):
	result_string = ''
	
	for i in text :
		ascii_value = ord(i);
		if(64<ascii_value <91):
			result_string += chr(ascii_value + 32)
		else:
			result_string += i
	return result_string
	
	

# Convert the string into capital case	
def capital_case(text):
	result_string = ''
	
	for i in text :
		ascii_value = ord(i);
		if(96 < ascii_value < 123):
			result_string += chr(ascii_value - 32)
		else:
			result_string += i
	return result_string

# Reverse the case of the string.
def string_swap_case(text):
	result_string=''
	
	for i in range(len(text)):
		if(ord(text[i])<91):
			result_string += small_case(text[i])
		else:
			result_string += capital_case(text[i])
	
	return result_string
		
'''
# Reverse the original string	
def reverse_string(text):
	result_string = ''
	
	for i in range(len(text)-1,-1,-1):
		result_string += text[i]
	
	return result_string
'''	

# Zig Zag pattern is form where alternative letter has same case ( small , capital )
def zig_zag_pattern(text):
	result_string = ''
	
	if(ord(text[0])<91):
		for i in range (len(text)):
			if(i%2!=0):
				result_string += small_case(text[i])
			else:
				result_string += capital_case(text[i])
				
	else:
		for i in range (len(text)):
			if(i%2!=0):
				result_string += capital_case(text[i])
			else:
				result_string += small_case(text[i])
	
	
	return result_string
	

# Pattern formed using the builtins function of string class
'''
def zig_zag_pattern_using_builtins(text):
	result_string = ''
	
	if(ord(text[0])<91):
		for i in range (len(text)):
			if(i%2!=0):
				result_string += text[i].lower()
			else:
				result_string += text[i].upper()
				
	else:
		for i in range (len(text)):
			if(i%2!=0):
				result_string += text[i].upper()
			else:
				result_string += text[i].lower()
	
	
	return result_string
'''

'''
#another approach of reversing the string .
def reverse_string_2(text):
		string = ''
		l=(len(text)-1)
		
		while(l>=0):
			string += text[l]
			l-=1
			
			
		return string
			
	'''

# function for calling different style and run the funciton
def change_case(text,style):
	if(style == 's' or style == 'S'):
		 return small_case(text)
	
	if(style == 'c' or style == 'C'):
		 return capital_case(text)
	
	if(style == 'r' or style == 'R'):
		 return string_swap_case(text)
		
	if(style == 'z' or style == 'Z'):
		 return zig_zag_pattern(text)
	
	else:
		return "Invaild Style"


print(change_case("aNghJOr#@annnn1234@#$@$%#2",'c'))

