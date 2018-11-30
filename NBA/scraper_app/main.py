from datetime import date, timedelta
from multiprocessing import Pool

from scraper import get_game_links, get_daily_data
from helpermethods import get_last_processing_date, update_processing_date


# Get last processing date(+1) and make payload for GET request, loop through days until yesterdays date is hit
base_url = 'https://www.basketball-reference.com/boxscores'
days_forward = 1
while True:
	yesterdays_date = date.today() - timedelta(1)
	date = get_last_processing_date() + timedelta(days_forward)
	payload = {'month': str(date.month), 'day': str(date.day), 'year': str(date.year)}
	links = get_game_links(base_url, payload)
	print(links)
# 	with Pool as p:
# 		p.map(links, get_daily_data())
	if date == yesterdays_date:
		update_processing_date(date.strftime('%Y-%m-%d'))
		break
	else:
		days_forward += 1