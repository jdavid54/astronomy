# class date n'existe pas

import datetime  # datetime is a subclass of date : class datetime(date)
print(type(datetime))
'''
Class datetime methods defined here:
     |  
     |  combine(...) from builtins.type
     |      date, time -> datetime with same date and time fields
     |  
     |  fromisoformat(...) from builtins.type
     |      string -> datetime from datetime.isoformat() output
     |  
     |  fromtimestamp(...) from builtins.type
     |      timestamp[, tz] -> tz's local time from POSIX timestamp.
     |  
     |  now(tz=None) from builtins.type
     |      Returns new datetime object representing current time local to tz.
     |      
     |        tz
     |          Timezone object.
     |      
     |      If no tz is specified, uses local timezone.
     |  
     |  strptime(...) from builtins.type
     |      string, format -> new datetime parsed from a string (like time.strptime()).
     |  
     |  utcfromtimestamp(...) from builtins.type
     |      Construct a naive UTC datetime from a POSIX timestamp.
     |  
     |  utcnow(...) from builtins.type
     |      Return a new datetime representing UTC day and time.
'''
from datetime import datetime, timedelta
print('typeof datetime',type(datetime))
print('typeof now',type(datetime.now))
print('typeof ctime',type(datetime.ctime))
print('typeof isocalendar',type(datetime.isocalendar))
print('ctime',datetime.ctime)
#print('ctime()',datetime.ctime())

print('=============================================================')
# sytem date & time
# class methods : use datetime.method()
print('now()',datetime.now())
print('today',datetime.today())

# date is an local instance of datetime
date = datetime.strptime('2020-11-16 11:57:00','%Y-%m-%d %H:%M:%S')
print(type(date))
# instance attributes
print(date.year, date.month, date.day)
# instance methods : use instance.method()
y, w, wd = date.isocalendar()
print('isocalendar()',w,wd)
print('isoformat()', date.isoformat())
print('ctime()',date.ctime())
wd = date.isoweekday()  #1=monday
print('isoweekday()',wd)

#date2 = datetime.strptime('1954-09-21 0:0:0','%Y-%m-%d %H:%M:%S')
print('toordinal()',date.toordinal())
print('weekday',date.weekday())  #0=monday

print('timedelta()',timedelta(days=1, seconds=45))

# replace
date = date.replace(hour=11, minute=42)
print('ctime()',date.ctime())
#timetuple
print('timetuple()',date.timetuple())

import time
print('time()',time.time())
# class methods
date2 = datetime.fromtimestamp(time.time())
print('ctime()',date2.ctime())