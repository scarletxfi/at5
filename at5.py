#at5 - Atomic Time 5(min). Add 5 minutes to current NTP (or atomic) time

from datetime import datetime, timedelta
from time import ctime
from colorama import init, Fore
import time
import ntplib
import platform
import os
import sys

os.system("cls")

print('System OS: ' + platform.system() + ' ' + platform.version())

#gets current ntp time
def getNTPDateTime(server):
    try:
        ntpDate = None
        client = ntplib.NTPClient()
        response = client.request(server, version=3)
        response.offset
        ntpDate = ctime(response.tx_time)
        #print the origin timestamp
        print('ntp request: ' + ntpDate)
    except Exception as e:
        print (e)
    return datetime.strptime(ntpDate, '%a %b %d %H:%M:%S %Y')

#note: time.google.com uses leap second smearing
ntp_timenow = getNTPDateTime(server='time.google.com')
print(  )

#add 5 minutes in microseconds to actual time
at_five_adj = ntp_timenow + timedelta(microseconds=300000000)

#define the current and adjusted time & date as a string so there is only 1 ntp request
current_timeDateString = str(ntp_timenow)
adjusted_timeDateString = str(at_five_adj)

#format is now YYYY-MM-DD HH:MM:SS
timeDateFormat = '%Y-%m-%d %H:%M:%S'
timeFormat = '%H:%M:%S'

#define 1 second in +microseoncds to increment
sec = timedelta(microseconds=+1000000)

#add 1 second in microseconds to current and adjusted time
currentTime = datetime.strptime(current_timeDateString, timeDateFormat) + sec
adjustedTime = datetime.strptime(adjusted_timeDateString, timeDateFormat) + sec

while True:

    #print at5 time with some color (for fun), and end with a carriage return
    print(Fore.YELLOW + 'Current time: ' + str(currentTime))
    print(Fore.GREEN +  'at5:          ' + str(adjustedTime), end='\r')
           
    #move cursur up by 2 lines so that the time output gets overwritten
    sys.stdout.write('\033[F')
    sys.stdout.write('\033[F')
    
    print(  )
       
    #add 1 second in microseconds to actual and adjusted time
    currentTime = currentTime + sec
    adjustedTime = adjustedTime + sec

    #wait for 1 second before going again
    time.sleep(1)
