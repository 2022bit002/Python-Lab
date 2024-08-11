def calender_print(dd,mm,yyyy):
	day = ['sat','sun','mon','tues','wed','thurs','fri']
	month = [0, 1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
	year ={16:6,17:4,18:2,19:0,20:6,21:4,22:2,23:0}
	
	d,m,y = dd,mm,yyyy
	
	y2 = y%100
	y1 =y//100
	quoient = y2//4
		
	
	
	
	sum = d + month[m] + year.get(y1) + y2 + quoient
	
	final=sum%7
	
	if(y%4==0 and (m==1 or m==2)):
		final=final-1
		
	
	return day[final]
	
	
print(calender_print(1,1,2004))
	
