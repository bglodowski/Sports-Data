import pymysql
import sshtunnel

USERNAME = 'bglodowski'
PASSWORD =
HOST =
DB =

def get_connection():
    try:
        conn = pymysql.connect(host=HOST,
        password=PASSWORD,
        user=HOST,
        db=db)

        return conn
    except Exception as e:
        with