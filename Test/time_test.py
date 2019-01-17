##################
#time_test
#Author:@Rooobins
#Date:2019-01-03
##################

import time

a = "Sat Mar 28 22:24:24 2016"

print(time.time())

print(time.localtime(time.time()))

print(time.asctime(time.localtime(time.time())))

print(time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime()))

print(time.strftime("%a %b %d %H:%M:%S",time.localtime()))

print(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))