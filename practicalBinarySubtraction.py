# Function to convert a binary string to integer

def to_int(text):
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

def str_to_int(text):
   
    text = text.lstrip('0')
    
    if not all(char in '01' for char in text):
        return "Invalid Input"
    length = len(text)
    num,n = 0,length - 1    
    if length == 0:
        return 0
    for i in range(length):
        bit = to_int(text[i])  
        num += bit * (2 ** n) 
        n -= 1

    return num

# Function to convert an integer to binary string
def to_binary_str(num):
    if num == 0:
        return '0'
    binary_str = ''
    while num > 0:
        binary_str = str(num % 2) + binary_str
        num = num // 2
    return binary_str

# Function to perform binary subtraction
def binary_subtraction(bin_str1, bin_str2):
    
    num1 = str_to_int(bin_str1)
    num2 = str_to_int(bin_str2)
    
    if isinstance(num1, str) or isinstance(num2, str):
        return "Invalid Input"  # If either input is invalid

    # Subtract the two numbers
    result = num1 - num2
    
    # If the result is negative, return error for binary context
    if result < 0:
        return "Negative Result (Not representable in binary)"
    
    # Convert the result back to a binary string
    return ""+to_binary_str(result)


str1 = "1111" 
str2 = "111"   

print(binary_subtraction(str1, str2))  




