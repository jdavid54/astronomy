# link : https://docs.python.org/3/library/datetime.html#datetime.tzinfo

import datetime

# constants
print(datetime.MINYEAR)
print(datetime.MAXYEAR)

# classes
print(datetime.date)
print(datetime.time)
print(datetime.datetime)
print(datetime.timedelta)
print(datetime.tzinfo)
print(datetime.timezone)

# instancing class

######## class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)¶
from datetime import timedelta  # import function 
delta = timedelta(
    days=50,              # 50 days
    seconds=27,           # 27 s
    microseconds=10,      # 10 us
    milliseconds=29000,   # 29 s
    minutes=5,            # 5 mn
    hours=8,              # 8 h
    weeks=2               # 14 days
)
print(delta)

d = timedelta(microseconds=-1)
print(d)

# class timedelta
# attributs 
print(timedelta.min)
print(timedelta.max)
print(timedelta.resolution)

d = timedelta(hours=-5)
print(d)
d = datetime.timedelta(days=-1, seconds=68400)
print(d)

delta1 = timedelta(seconds=57)
delta2 = timedelta(hours=25, seconds=2)
print(delta1)
print(delta2)
t = (delta2 != delta1)
print(t)
t = (delta2 == 5)
print(t)

# methods
year = timedelta(days=365)   # instance with argument days
print(year.total_seconds())  # method

another_year = timedelta(weeks=40, days=84, hours=23, minutes=50, seconds=600)
t = (year == another_year)
print(t)
print(another_year.total_seconds()) 

######### class date is a subclass of datetime
# class datetime.date(year, month, day)
from time import time  # import function time()
from datetime import date

# attributs
d1 = date(1954, 9, 21)
print('instance=',d1, type(d1))   # isoformat class datetime.date
iso = date.fromisoformat(str(d1))
print('iso format=',iso, type(iso)) # class datetime.date

print('min',date.min)    # class datetime.date
print(d1.max)
print(d1.resolution)     # class datetime.timedelta
print(d1.year)           # int
print(d1.month)          # int
print(d1.day)            # int


# method today()
print(date.today())
# method fromtimestamp
t = time()       # timestamp
print('t=',t)
print(date.fromtimestamp(t))
# method fromisoformat
s = '2019-12-04' # isoformat string
print(date.fromisoformat(s))
# method fromordinal
print(date.fromordinal(1))   # year 0001, month 1, day 1
print(date.fromordinal(366)) # year 0002, month 1, day 1
# instancing timedelta class
d = timedelta(days=-365*45, seconds=-1)
print(d)
# method replace()
d = date(2002, 12, 31)
d.replace(day=26)
print('not replaced',d)
d = d.replace(day=26)
print('need explicite affectation to be replaced',d)
# methode timetuple()
print('tuple', d.timetuple())   # time.struct_time
# time.struct_time
#(tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst)

# method toordinal()
# method weekday()
# method isoweekday()
print(date(2020,1,1).weekday())
# method isocalendar()
legend='''\
For example, 2004 begins on a Thursday, so the first week of ISO year 2004 \
begins on Monday, 29 Dec 2003 and ends on Sunday, 4 Jan 2004'''
d = date(2003, 12, 29).isocalendar()   # week 1 of 2004 even if the date is 2003
print(d)
d = date(2004, 1, 4).isocalendar()
print(d, type(d))

# not named tuple : d.year -> error
print(d[1])

today = date.today()
print(today)

# methode ctime
d = date(2020, 12, 16)
print(d.ctime())

# example of usage
print('Examples 1')
t = (today == date.fromtimestamp(time()))
print(t)

my_birthday = date(today.year, 9, 21)
if my_birthday < today:
    my_birthday = my_birthday.replace(year=today.year + 1)
print('next birthday :', my_birthday)

time_to_birthday = abs(my_birthday - today)
print('days to my bday:',time_to_birthday.days)

d = date.fromordinal(730920) # 730920th day after 1. 1. 0001
print(d)   #datetime.date(2002, 3, 11)

# Methods related to formatting string output
print('datetime methods')
print(d.isoformat())  #'2002-03-11'
print(d.strftime("%d/%m/%y"))   #'11/03/02'
print(d.strftime("%A %d. %B %Y"))  #'Monday 11. March 2002'
print(d.ctime())   #'Mon Mar 11 00:00:00 2002'
text = 'The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month")
print(text)   #'The day is 11, the month is March.'

# Methods for to extracting 'components' under different calendars
t = d.timetuple()
for i in t:     
    print(i)

ic = d.isocalendar()
for i in ic:    
    print(i)
'''
2002                # ISO year
11                  # ISO week number
1                   # ISO day number ( 1 = Monday )
'''
# A date object is immutable; all operations produce a new object
print(d)
print(d.replace(year=2005))  # new object : datetime.date(2005, 3, 11))
print(d)   # unchanged

######### class datetime is a subclass of datetime with timezone, utc
# class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
from time import time  # import function time()
from datetime import datetime # import function if not must write datetime.datetime()

print(datetime.today())   # localtime
print(datetime.utcnow())  # utc time

print(datetime.fromtimestamp(time()))  # time() -> timestamp as float

print(datetime.utcfromtimestamp(time()))  # utc

print(datetime.fromordinal(100))  # arg int

# classmethod datetime.combine(date, time, tzinfo=self.tzinfo)¶
print(d,datetime.combine(d, datetime.time(datetime(2014,12,1,8,15,20))))
# YYYY-MM-DD[*HH[:MM[:SS[.fff[fff]]]][+HH:MM[:SS[.ffffff]]]]
print(datetime.fromisoformat('2014-12-21*12:05:45'))

print(datetime.fromisoformat('2014-12-21+11:05:08'))

# example
print('Examples 2')
d = datetime.fromisoformat('2011-11-04')
print(d)
d = datetime.fromisoformat('2011-11-04T00:05:23')
print(d)
d = datetime.fromisoformat('2011-11-04 00:05:23.283')
print(d)
d = datetime.fromisoformat('2011-11-04 00:05:23.283+00:00')
print(d)
d = datetime.fromisoformat('2011-11-04T00:05:23+04:00')   
print(d)

# datetime attributs
print(datetime.min)
print(datetime.max)
print(datetime.resolution)
print(datetime.year)
print(datetime.month)
print(datetime.day)
print(datetime.hour)
print(datetime.minute)
print(datetime.second)
print(datetime.microsecond)
print(datetime.tzinfo)
print(datetime.fold)

# instance methods
print('d=',d)
print(datetime.date(d))
print(datetime.time(d))
print(datetime.timetz(d))

print(d.replace(year=2020))

# need an instance of datetime
d = datetime(2019, 5, 18, 15, 17, 8, 132263)
print(d.astimezone())
print(d.utcoffset())
print(d.dst())
print(d.tzname())
print(d.utctimetuple())

print(d.toordinal())
print(d.timestamp())

print(d.weekday())
print(d.isoweekday())
print(d.isocalendar())
print(d.isoformat())

print(datetime.now().isoformat(timespec='minutes')   )

# datetime.isoformat(sep='T', timespec='auto')
dt = datetime(2015, 1, 1, 12, 30, 59, 0)
print(dt, dt.isoformat(sep='X'))   # timespec = 'auto'
print(dt, dt.isoformat(timespec='microseconds')) # include microseconds

from datetime import tzinfo, timedelta, datetime, timezone

# class TZ with method utcoffset
class TZ(tzinfo):  # a subclass of tzinfo
    """A time zone with an arbitrary, constant -06:39 offset."""
    def utcoffset(self, dt):
        #return None
        return timedelta(hours=-6, minutes=-39)  # string '-6:39' is added to date and time
    def dst(self, dt):
        return timedelta(hours=1)        
    def tzname(self, dt):
        return 'USA, New York'

print('TZ info')

'''
Return a string representing the date and time in ISO 8601 format:
YYYY-MM-DDTHH:MM:SS.ffffff, if microsecond is not 0
YYYY-MM-DDTHH:MM:SS, if microsecond is 0

If utcoffset() does not return None, a string is appended, giving the UTC offset:
YYYY-MM-DDTHH:MM:SS.ffffff+HH:MM[:SS[.ffffff]], if microsecond is not 0
YYYY-MM-DDTHH:MM:SS+HH:MM[:SS[.ffffff]], if microsecond is 0
'''
d = datetime(2002, 12, 25, tzinfo=TZ()).isoformat(' ')
print(d)
d = datetime(2009, 11, 27, microsecond=100, tzinfo=TZ()).isoformat()
print(d)

d = datetime.now().isoformat(timespec='minutes')   # HH:MM
print(d)
dt = datetime(2015, 1, 1, 12, 30, 59, 0)
print(dt, dt.isoformat(timespec='microseconds'))   # HH:MM:SS:ffffff

d = datetime(2002, 12, 25, tzinfo=TZ())
print('as time zone:',d.astimezone())
print('utc offset:',d.utcoffset())
print('dst:', d.dst())
print('tzname:', d.tzname())
print('utc time tuple:', d.utctimetuple())

# example Timezone
print('Example 3')


#from datetime import timedelta, datetime, tzinfo, timezone
# subclass 
class KabulTz(tzinfo):
    # Kabul used +4 until 1945, when they moved to +4:30
    UTC_MOVE_DATE = datetime(1944, 12, 31, 20, tzinfo=timezone.utc)

    def utcoffset(self, dt):
        if dt.year < 1945:
            return timedelta(hours=4)
        elif (1945, 1, 1, 0, 0) <= dt.timetuple()[:5] < (1945, 1, 1, 0, 30):
            # An ambiguous ("imaginary") half-hour range representing
            # a 'fold' in time due to the shift from +4 to +4:30.
            # If dt falls in the imaginary range, use fold to decide how
            # to resolve. See PEP495.
            return timedelta(hours=4, minutes=(30 if dt.fold else 0))
        else:
            return timedelta(hours=4, minutes=30)

    def fromutc(self, dt):
        # Follow same validations as in datetime.tzinfo
        if not isinstance(dt, datetime):
            raise TypeError("fromutc() requires a datetime argument")
        if dt.tzinfo is not self:
            raise ValueError("dt.tzinfo is not self")

        # A custom implementation is required for fromutc as
        # the input to this function is a datetime with utc values
        # but with a tzinfo set to self.
        # See datetime.astimezone or fromtimestamp.
        if dt.replace(tzinfo=timezone.utc) >= self.UTC_MOVE_DATE:
            return dt + timedelta(hours=4, minutes=30)
        else:
            return dt + timedelta(hours=4)

    def dst(self, dt):
        # Kabul does not observe daylight saving time.
        return timedelta(0)

    def tzname(self, dt):
        if dt >= self.UTC_MOVE_DATE:
            return "+04:30"
        return "+04"
    
# instance
tz1 = KabulTz()

# Datetime before the change
dt1 = datetime(1900, 11, 21, 16, 30, tzinfo=tz1)
print(dt1.utcoffset())


# Datetime after the change
dt2 = datetime(2006, 6, 14, 13, 0, tzinfo=tz1)
print('kabul:', dt2, dt2.utcoffset())


# Convert datetime to another time zone
dt3 = dt2.astimezone(timezone.utc)
print('utc:', dt3)

dt2

dt2 == dt3