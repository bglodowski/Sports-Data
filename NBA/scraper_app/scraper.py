from bs4 import BeautifulSoup
import requests


def get_soup(params=None):
	try:
		response = requests.get('https://www.basketball-reference.com/boxscores', params)
		soup = BeautifulSoup(response)
	except ConnectionError:
		print('Unable to connect to website.')
	except TimeoutError:
		print('Unable to connect, connection timed out.')
	return soup


def get_daily_data(payload):
	links = []
	soup = get_soup(payload)
	for link in soup.find_all('a', string='Box Score'):
		links.append(link.get('href'))
	return links




def get_game_links(soup):
	return None