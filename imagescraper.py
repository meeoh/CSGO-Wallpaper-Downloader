from bs4 import BeautifulSoup
import requests
import urllib
import os




def download(soup):
	for link in soup.find_all("img"):
		global counter
		dl = "http://www.mossawi.nl/csgo/" + link['src'].replace('thumbnails','original')
		urllib.urlretrieve(dl,"csgoBackgrounds/csgoBackground" + str(counter) + ".png")
		counter += 1

#counter for pic nubmer
counter = 1

#this is the folder that the pics will be saved in
newpath = os.getcwd() + "\csgoBackgrounds"

#if it doesnt exist, make it
if not os.path.exists(newpath):
    os.makedirs(newpath)


#make one initial call to find how many pages there are
url = "http://www.mossawi.nl/csgo/"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "html.parser")
#set the number of pages
numPages = len(soup.find_all("a", class_="pagination-item"))

#loop through amount of pages
i = 1
while(i <= numPages):

	#first page link doesnt have a part in the url
	if (i == 1):
		url = "http://www.mossawi.nl/csgo/"
	else :
		url = "http://www.mossawi.nl/csgo/?page=" + str(i)

	#download all the pics on that page
	r = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data, "html.parser")
	download(soup)
	#increment to next page
	i += 1