import time




def get_even_odd_count0(I):
	even_count, odd_count= 0, 0
	for i in I:
		if i%2 !=0 :
			odd_count +=1
		else:
			even_count +=1
	return even_count, odd_count
	
def get_even_odd_count1(I):
	even_count , odd_count =0, 0
	for i in I:
		if i%2:
			odd_count +=1
		else:
			even_count +=1
	return even_count, odd_count
	
def get_even_odd_count2(I):
	even_count, odd_count = 0, 0
	for i in I:
		if i&1:
			odd_count +=1
		else:
			even_count +=1
	return even_count, odd_count
	
def get_even_odd_count3(I):
	even_count, odd_count,t = 0, 0, 0
	for i in I:
		t = i%2
		odd_count += t
		even_count += 1-t
	return even_count, odd_count
	
def check_the_time(I):

	start = time.time()
	get_even_odd_count0(I)
	end = time.time()
	base0 = start - end
	start = time.time()
	get_even_odd_count1(I)
	end = time.time()
	base1 = start - end
	start = time.time()
	get_even_odd_count2(I)
	end = time.time()
	base2 = start - end
	start = time.time()
	get_even_odd_count3(I)
	end = time.time()
	base3 = start - end
	
	base1 = ((base0-base1)/base0)*100
	base2 = ((base0-base2)/base0)*100
	base3 = ((base0-base3)/base0)*100
	print("Approach 2 is faster",base1,"% than 1 approach ")
	print("Approach 3 is faster ",base2,"% than 1 approach ")
	print("Approach 4 is faster ",base3,"% than 1 approach ")
	
	
	
check_the_time([1,2,3,4,5,6,7,8])





