	
	
	
def print_cal(day,month,yy):
	days_month = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
	week_day = ['sun', 'mon','tue','wed','thur','fri','sat']
	first_day ={'sun':0,'mon':1,'tue':2,'wed':3,'thur':4,'fri':5,'sat':6}
	gap_day ={'sun':'      '*0,'mon':'      '*1,'tue':'      '*2,'wed':'      '*3,'thur':'      '*4,'fri':'      '*5,'sat':'      '*6}
	month_dic = {1:'jan',2:'feb',3:'mar',4:'april',5:'may',6:'june',7:'july',8:'august',9:'september',10:'october',11:'november',12:'december'}
	print(yy)
	print(month_dic[month])
	for i in week_day:
		print(i,end='   ')
		
	print()
	k=(first_day['sat']-first_day[day]+1)%7
	for i in range(1,days_month[month]+1):
		if i==1:
			print(end=gap_day[day])
		if i<10: 
			print(0,end='')
		
		print(i,end='    ')
		if i%7==k:
			print()
			
			
	print()
		

	
def calender_print(mm,yyyy,dd=1):
	day = ['sat','sun','mon','tue','wed','thur','fri']
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
		
	
	print_cal(day[final],mm,yyyy)


for i in range(1,13):
	calender_print(i,2024)	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
