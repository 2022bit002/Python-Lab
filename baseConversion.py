def changeBaseFunction( text , basetext = 3 , changebase = 10):
	length = len(text)
	power=0
	final_num=0
	for i in range(length-1,-1,-1):
		nums = int(text[i])
		#print(nums)
		final_num += nums * pow(basetext,power)
		power+=1
	print(final_num)
	
	
changeBaseFunction('11')
		
		
		
		
				
