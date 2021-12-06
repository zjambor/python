import cx_Oracle
import config_cloud as cfg
from tabulate import tabulate
import datetime

try:
    conn = cfg.connection
except cx_Oracle.Error as error:
    print(error)

print (conn.version)
ver = conn.version.split(".")             

c = conn.cursor()

check_conn = c.execute('select 1 from dual')
check_conn_result = check_conn.fetchone()[0]
print (check_conn_result)