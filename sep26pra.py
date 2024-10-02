
def string_valid(l):
	d,n = {}, ''
	m = ['a','e','i','o','u']
	for i in l:
		if i in m:
			if i in d:
				d[i]+=1
			else:
				d[i] = 1
				n = i
	if n=='':
		return 1
	w = d[n] 
	for i in d:
		if d[i]!=w:
			return 0
	return 1

def get_string_count(I):
	valid = 0
	for i in I:
		if isinstance(i,str):
			valid += string_valid(i)
		elif isinstance(i,(list,tuple,set)):
			valid += get_string_count(i)
	return valid
	
	
	
print(get_string_count(['pankaj','om','even','rutwiki']))
