import cx_Oracle
import config as cfg
from tabulate import tabulate
import datetime

try:
    conn = cx_Oracle.connect(cfg.user, cfg.password, dsn=cfg.dsn_tns, encoding="UTF-8") 
except cx_Oracle.Error as error:
    print(error)

print (conn.version)
ver = conn.version.split(".")             

c = conn.cursor()

check_conn = c.execute('select 1 from dual')
check_conn_result = check_conn.fetchone()[0]
print (check_conn_result)

table = []
headers = ["Empno", "Ename", "Job", "MGR", "Hiredate", "sal", "comm", "Deptno"]

c.execute('select employee_id,last_name,job_id,manager_id,hire_date,salary,commission_pct,department_id from employees') # use triple quotes if you want to spread your query across multiple lines
for row in c:
    thislist = []
    empno = row[0]
    ename = row[1]
    job = row[2]
    mgr = row[3]
    hiredate = row[4]
    sal = row[5]
    comm = row[6]
    deptno = row[7]
    thislist.append(empno)
    thislist.append(ename)
    thislist.append(job)
    thislist.append(mgr)
    thislist.append(hiredate.strftime("%Y.%m.%d"))
    thislist.append(sal)
    thislist.append(comm)
    thislist.append(deptno)
    table.append(thislist)

print("")
print(tabulate(table, headers=headers))
print("") 
conn.close()

def cursor(s):
    try:
        conn = cx_Oracle.connect(cfg.user, cfg.password, dsn=cfg.dsn_tns) 
    except cx_Oracle.Error as error:
        print(error)
    table = []
    c = conn.cursor()
    c.execute(s)
    for row in c:
        thislist = []
        empno = row[0]
        ename = row[1]
        job = row[2]
        mgr = row[3]
        hiredate = row[4]
        sal = row[5]
        comm = row[6]
        deptno = row[7]
        thislist.append(empno)
        thislist.append(ename)
        thislist.append(job)
        thislist.append(mgr)
        thislist.append(hiredate.strftime("%Y.%m.%d"))
        thislist.append(sal)
        thislist.append(comm)
        thislist.append(deptno)
        table.append(thislist)
    conn.close()
    return len(table)

print("Number of rows:", cursor('select employee_id,last_name,job_id,manager_id,hire_date,salary,commission_pct,department_id from employees'))