from datetime import datetime


def get_last_processing_date():
	try:
		with open('lastprocessingdate.txt') as f:
			last_day = f.read()
			return datetime.strptime(last_day, "%Y-%m-%d").date()
	except FileNotFoundError:
		print("File cannot be found.")



def update_processing_date(processing_date):
	try:
		with open('lastprocessingdate.txt', 'w')as f:
			f.write(processing_date)
	except FileNotFoundError:
		print("File cannot be found.")