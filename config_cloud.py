import cx_Oracle
import os

user='admin'
password='szaolikK9595'

dsn_tns = """(description= (retry_count=20)(retry_delay=3)(address= (protocol=tcps)(port=1522)
(host=adb.eu-frankfurt-1.oraclecloud.com))
(connect_data=(
service_name=gu9d7xztta04lxm_db202005081825_high.atp.oraclecloud.com))
(security=(ssl_server_cert_dn="CN=adwc.eucom-central-1.oraclecloud.com,OU=Oracle BMCS FRANKFURT,O=Oracle Corporation,L=Redwood City,ST=California,C=US")))"""

connection = cx_Oracle.connect(user, password, dsn_tns, encoding="UTF-8")
