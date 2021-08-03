import datetime
from datetime import date
from real_time import ht, mt, st
import sys

try:
	name = sys.argv[1]
	y = int(sys.argv[2])
	m = int(sys.argv[3])
	d = int(sys.argv[4])
	def inf(name, y, m ,d):

		border = "=" * 100

#main
		today = datetime.date.today()
		bday_day = datetime.date(y, m, d)
		much = today - bday_day
		months_lived = much.days // 30
		weeks = much.days // 7
		hours = much.days * 24
		minuts = hours * 60
		seconds = minuts * 60
		age = today.year - bday_day.year
#print	
		print(border)
		print("{} is now {}".format(name, age))
		print("He Lived {} days {} months {} weeks {} hours , {} minuts and {} seconds".format(much.days, months_lived, weeks, ht, mt, st))
		print('Happy Birthday {}'.format(name))
		print(border)
	inf(name, y, m, d)
except:
	print('Error : python3 bday.py [name] [year] [month] [day]')


