#This program will request the webpage nytimes.com and 
#print a list of all the article headlines.

from bs4 import BeautifulSoup
from bs4 import NavigableString
from urllib.request import urlopen

doc = urlopen("http://nytimes.com").read()
#print(doc)
soup = BeautifulSoup(doc, "html.parser")
print(soup.title.text)
title_list = soup.select(".story-heading")
for item in title_list:
	if(item.string != 'None'):
		print(item.text.strip())
