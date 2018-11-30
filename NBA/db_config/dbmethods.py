import pymysql

try:
	conn = pymysql.connect(
		'nbadatabase.cd8o3ycjw7ei.us-east-2.rds.amazonaws.com',
		user='bglodowski',
		passwd='Brain11!',
		db='nbadatabase'
	)
except TimeoutError:
	print("Unable to connect to MySQL database.")

with conn.cursor() as cur:
	cur.execute("SELECT VERSION()")
	version = cur.fetchone()
	print("Database version: {}".format(version))
