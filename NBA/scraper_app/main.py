from datetime import date, timedelta

from scraper import get_soup

# Get yesterdays date and make payload for GET request
date = date.today() - timedelta(1)
payload = {'month': str(date.month), 'day': str(date.day), 'year': str(date.year)}
soup = get_soup(payload)

#this is a test

