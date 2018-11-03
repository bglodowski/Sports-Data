from datetime import date, timedelta


# Get yesterdays date
date = date.today() - timedelta(1)
payload = {'month': str(date.month), 'day': str(date.day), 'year': str(date.year)}
daily_base = 'https://www.basketball-reference.com/boxscores'