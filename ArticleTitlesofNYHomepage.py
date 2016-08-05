#This program will request the webpage nytimes.com and 
#print a list of all the article headlines.

from bs4 import BeautifulSoup
from urllib.request import urlopen

doc = urlopen("http://nytimes.com").read()
print (doc)
