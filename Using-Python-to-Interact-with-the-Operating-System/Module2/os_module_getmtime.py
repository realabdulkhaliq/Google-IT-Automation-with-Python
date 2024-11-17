import os
import datetime

os.path.getmtime("spider.txt")
#This code will provide a unix timestamp for the file

timestamp = os.path.getmtime("spider.txt")
datetime.datetime.fromtimestamp(timestamp)
#This code will provide the date and time for the file in an 
#easy-to-understand format

print(datetime.datetime.fromtimestamp(timestamp))