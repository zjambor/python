import cx_Oracle

hostname = 'cenaicst1'
port = 1521
service_name='testdb3'
user=r'iamedy'
password='iamedy'

dsn_tns = cx_Oracle.makedsn(hostname, port, service_name) # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
