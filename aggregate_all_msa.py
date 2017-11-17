import urllib2
import time
months = ['01','02','03','04','05','06','07','08','09','10','11','12']
#months = ['01']
year = '16'
url_beginning = "https://www2.census.gov/econ/bps/Metro/ma"
url_end = "c.txt"
for month in months:
        response = urllib2.urlopen(url_beginning + year + month + url_end)
        html = response.read()
        html = html.splitlines()
        for line in html:
                print line
        time.sleep(5)#don't overload server

