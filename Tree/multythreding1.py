import thread
import time


def print_time(Name, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % (Name, time.ctime(time.time()) )
try:
   thread.start_new_thread( print_time, ("Thread-1", 3, ) )
   thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print ("Error")

while 1:
   pass