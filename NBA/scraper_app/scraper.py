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


#######################COPIED FROM OLD PROGRAM##########################################

def get_player_stats(soup):
	# Gets team acronym (away team index[0] home team index[1]
	teams = soup.find_all('span')
	team_list = []
	for team in teams:
		if team.strong and len(team.strong.string) == 3:
			team_list.append(team.strong.string)

	# Get table stats into list of list for each row
	tables = soup.find_all("tbody")
	master_list = []
	for table in tables:
		rows = table.find_all('tr')
		for row in rows:
			player_stats = []
			if row == rows[5]:  # 5th row contains mid table headers not data, causes error
				continue
			else:
				name = row.th.string
				player_stats.append(name)
				if table == tables[0]:
					player_stats.append(team_list[0])  # player team listed followed by opponent
					player_stats.append(team_list[1])
				elif table == tables[2]:
					player_stats.append(team_list[1])  # player team listed followed by opponent
					player_stats.append(team_list[0])
				stats = row.find_all('td')
				for stat in stats:
					data = stat.string
					if data is None:
						data = ' '
					player_stats.append(data)
			master_list.append(player_stats)
	return master_list


# Combines multiple player list into 1 list for each player
def stat_combiner(stats):
	master = []
	stats.sort()        # sort list so both list listed in a row
	for i in range(0, len(stats), 2):  # Combines two list, second list is first table when sorted
		combined = stats[i + 1] + stats[i][2:]
		master.append(combined)
	return master


# Gets team stats for single day
def get_team_stats(soup):
	teams = soup.find_all('span')
	team_list = []
	for team in teams:
		if team.strong and len(team.strong.string) == 3:
			team_list.append(team.strong.string)

	tables = soup.find_all('tfoot')
	tables_stats = []

	for table in tables:
		data = []
		if table == tables[0]:
			data.append(team_list[0])  # player team listed followed by opponent
			data.append(team_list[1])
		elif table == tables[2]:
			data.append(team_list[1])  # player team listed followed by opponent
			data.append(team_list[0])
		stats = table.find_all('td')
		for stat in stats:
			data.append(stat.string)
		tables_stats.append(data)

	team_stats = []
	home_indicator = [['A'], ['H']]
	team_stats.append(tables_stats[0][0:2] + home_indicator[0] + tables_stats[0][3:21] + tables_stats[1][1:12] + tables_stats[1][13:])
	team_stats.append(tables_stats[2][0:2] + home_indicator[1] + tables_stats[2][3:21] + tables_stats[3][1:12] + tables_stats[3][13:])
	return team_stats