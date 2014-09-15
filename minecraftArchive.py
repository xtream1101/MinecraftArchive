from bs4 import BeautifulSoup
import re
import urllib2
import urllib

url="https://mcversions.net/"
request = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
page = urllib2.urlopen( request )
soup = BeautifulSoup(page.read())


mcReleases = soup.findAll('div',{'class':'box'})


for mcRelease in mcReleases:
	releaseName = mcRelease['id']
	mcVersions = mcRelease.findAll('div',{'class':'release'})
	for mcVersion in mcVersions:
		dlLinks = mcVersion.findAll('a')
		verison = mcVersion.find('h3')
		releaseDate = mcVersion.find('span',{'class':'time'})
		for link in dlLinks:
			fixedDate = releaseDate.string.split('/')
			fixedDate = fixedDate[2]+"."+fixedDate[0]+"."+fixedDate[1]
			jarFile = urllib.URLopener()
			jarFile.retrieve(link['href'], "Minecraft/"+fixedDate+"_"+releaseName+"_"+verison.string+"_"+link['class'][0]+".jar")

			print verison.string
			print fixedDate
			print releaseName
			print link['class'][0]
			print link['href']
			print "\n"

	#print mcRelease
	print "\n\n"