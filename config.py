import cx_Oracle

hostname = 'cenaicst2'
port = 1521
service_name='testdb'
user=r'hr'
password='hr'

dsn_tns = cx_Oracle.makedsn(hostname, port, service_name) # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
