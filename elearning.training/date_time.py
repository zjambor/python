from datetime import date, timedelta
from datetime import time
from datetime import datetime
import time as tm

d = date(2000, 5, 12)

print(d.year)
print(d.month)
print(d.day)

print(d.strftime("%Y %m %d"))

t = time(2, 30, 45)

print(t.hour)
print(t.minute)
print(t.second)

print(t.strftime("%H:%M:%S"))

dt = datetime(2000, 5, 22, 2, 30, 45)

print(dt.strftime("%Y-%m-%d %H:%M:%S"))

dt = datetime.now()
print(dt.strftime("%Y-%m-%d %H:%M:%S"))

add_dt = dt + timedelta(days=5)
print(add_dt.strftime("%Y-%m-%d %H:%M:%S"))

start = tm.time()
tm.sleep(1.5)
end = tm.time()
print(f"Took {end - start:3.3f} sec")

start = datetime.now()
tm.sleep(1.5)
end = datetime.now()
print(f"Took {(end - start).seconds}.{(end - start).microseconds} sec")
