#This program will request the webpage nytimes.com and 
#print a list of all the article headlines.

from bs4 import BeautifulSoup
from bs4 import NavigableString
from urllib.request import urlopen

#Open online html file
doc = urlopen("http://nytimes.com").read()

#Parse it into bS4
soup = BeautifulSoup(doc, "html.parser")

#Print webpage title to user
print(soup.title.text)

#Create a list with all the headline objects in the soup
title_list = soup.select(".story-heading")

#Open text file for output
open_file = open('headlines.txt', 'w')

#Print webpage title to text file
open_file.write(soup.title.text + "\n\n")

#Go through the list, printing the headlines to the output text file
for item in title_list:
	#Make sure that the item has a headline
	if(item.string != 'None'):
		open_file.write(item.text.strip() + "\n\n")

#Close output text file
open_file.close()
print("Done!")