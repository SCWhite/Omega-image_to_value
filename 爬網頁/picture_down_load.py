from urllib import urlretrieve
import time

# find yourself a picture on an internet web page you like
# (right click on the picture, look under properties and copy the address)

#http://www.cwb.gov.tw/V7/observe/radar/Data/HD_Radar/CV1_3600_201703101200.png
#print time.strftime("%Y%m%d%H%M", time.localtime())
count_time = time.strftime("%Y%m%d%H%M", time.localtime())
count_time = count_time[:-1] + '0'
#print count_time
string = "http://www.cwb.gov.tw/V7/observe/radar/Data/HD_Radar/CV1_3600_" + count_time + ".png"
print string
#string = string + 
url = string
filename = count_time + ".png"
# retrieve the image from the url and save it to file
urlretrieve(url, filename)
