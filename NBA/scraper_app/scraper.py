from bs4 import BeautifulSoup
import requests


def get_soup(params=None):
	try:
		response = requests.get('https://www.basketball-reference.com/boxscores', params)
		soup = BeautifulSoup(response.text, 'lxml')
	except ConnectionError:
		print('Unable to connect to website.')
	except TimeoutError:
		print('Unable to connect, connection timed out.')
	return soup


def get_daily_data(payload):
	return None



def get_game_links(payload):
	links = []
	soup = get_soup(payload)
	for link in soup.find_all('a', string='Box Score'):
	    tail = link.get('href')
	    url = 'https://www.basketball-reference.com{}'.format(tail)
	    links.append(url)
	return links