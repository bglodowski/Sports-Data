import pymysql
import sshtunnel

USERNAME = 'bglodowski'
PASSWORD =
HOST = 'bglodowski.mysql.pythonanywhere-services.com'
DB = 'bglodowski$NBA_DATA'

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

def get_connection():
    try:
        conn = pymysql.connect(host=HOST, user=USERNAME, password=PASSWORD, db=DB)
        return conn
    except Exception as e:
        with sshtunnel.SSHTunnelForwarder(('ssh.pythonanywhere.com'), ssh_username=USERNAME, ssh_password=PASSWORD, remote_bind_address=(HOST, 3306)) as tunnel:
            conn = pymysql.connect(host='127.0.0.1', port=tunnel.local_bind_port, user=USERNAME, password=PASSWORD, db=DB)
            return conn

def commit_data(cursor, stat_list):
    query = "INSERT INTO DAILY_NBA_ (id, )"


#TODO Add days since last game column