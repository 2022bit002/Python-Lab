def fun(x):
	for i in range(x+1):
		for j in range(x+1-i):
			print(' ',end='')
		for j in range(2*i+1):
			print('* ')
fun(2)
