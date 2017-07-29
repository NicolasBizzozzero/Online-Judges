#import datetime
#import calendar
from calendar import monthrange
from datetime import date

def add_month(sourcedate):
	month = sourcedate.month
	year = int(sourcedate.year + month / 12)
	month = month % 12 + 1
	day = min(sourcedate.day, monthrange(year, month)[1])
	return date(year, month, day)

if __name__ == '__main__':
	firstdate = date(1901, 1, 1)
	finaldate = date(2000, 12, 31)

	sundaycount = 0
	while (firstdate < finaldate):
		if(firstdate.day == 1 and firstdate.weekday() == 6):
			sundaycount += 1
		firstdate = add_month(firstdate)

	print(str(sundaycount))

