import sys
from hdbcli import dbapi

def connect1():
    connection = dbapi.connect('jamborz-hxe.westeurope.cloudapp.azure.com', 39013, 'system', 'szaolikK9595')

def connect():
    connection = dbapi.connect(
        'zeus.hana.prod.eu-central-1.whitney.dbaas.ondemand.com', 
        23803, 
        '6615F213C9084CFF99D36D2D64D3B301_5EGN5YY39OLN818P0EE57C1YG_RT', 
        'Wa30A.U5bqpOng4RzLeDLeTefaYvAszvkun26Lxt4yEgpIF4.RRUVY3xQ4c9YHFWk6itL_.B.UXRl.zvM8gtsTU_-4oPTh9EK0XvO-SmZ95u5N0TTocRebWPGSQ_mbww',
        # key=KEYNAME, # alternatively, use an HDB User Store Key for username, password (does not replace address, here)
        encrypt = 'true', 
        # sslCryptoProvider='openssl', 
        # sslTrustStore='/Users/cobra/.ssl/DigiCertGlobalRootCA.pem'
        #sslCryptoProvider='commoncrypto', 
        #sslTrustStore='$SECUDIR/sapcli.pse'
        )
    return connection

def check_conn(connection):
    sql = "select '1' from dummy"
    cursor = connection.cursor()
    cursor.execute(sql)
    res = cursor.fetchone()
    return res[0]

connection = connect()

with connection.cursor() as cursor:
	sql = "SELECT SYSTEM_ID, DATABASE_NAME, VERSION FROM M_DATABASE"
	cursor.execute(sql)
	result = cursor.fetchall()

print ("Connection to SAP HANA Service successful.")
print ("SID =", result[0][0])
print ("Database Name =", result[0][1])
print ("Version =", result[0][2])

def query(sqlstring):
    cursor = connection.cursor()
    cursor.execute(sqlstring)
    for row in cursor:
        print(row)

#sql = "SELECT DATABASE_NAME, SERVICE_NAME, PORT, SQL_PORT, (PORT + 2) HTTP_PORT FROM SYS_DATABASES.M_SERVICES WHERE (SERVICE_NAME = 'indexserver' and COORDINATOR_TYPE = 'MASTER') or SERVICE_NAME = 'xsengine';"
sql = "SELECT table_name FROM tables where table_name like 'SAP_%'"
query(sql)

sql = "select * from schemas"
query(sql)


sql = "SELECT * from 6615F213C9084CFF99D36D2D64D3B301.SAP_CAPIRE_BOOKSHOP_BOOKS"
query(sql)

connection.close()