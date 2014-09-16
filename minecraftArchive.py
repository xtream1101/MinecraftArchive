from bs4 import BeautifulSoup
import re
import os
import urllib2
import urllib

url="https://mcversions.net/"
VERSIONURL="https://s3.amazonaws.com/Minecraft.Download/versions/:VERSION:/:VERSION:.json"
request = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
page = urllib2.urlopen( request )
soup = BeautifulSoup(page.read())

if not os.path.exists("Minecraft"):
	os.mkdir("Minecraft")
	print "Created Minecraft directory"
if not os.path.exists("Minecraft/versions"):
	os.mkdir("Minecraft/versions")
	print "Created versions directory"
if not os.path.exists("Minecraft/servers"):
	os.mkdir("Minecraft/servers")
	print "Created servers directory"



mcReleases = soup.findAll('div',{'class':'box'})
for mcRelease in mcReleases: #loop through The release types
	releaseName = mcRelease['id']
	mcVersions = mcRelease.findAll('div',{'class':'release'})
	for mcVersion in mcVersions: # loop through each version in that release
		dlLinks = mcVersion.findAll('a')
		version = mcVersion.find('h3')
		releaseDate = mcVersion.find('span',{'class':'time'})
		for link in dlLinks: #download both the client and server files
			fixedDate = releaseDate.string.split('/')
			fixedDate = fixedDate[2]+"."+fixedDate[0]+"."+fixedDate[1]
			versionLink = VERSIONURL.replace(":VERSION:", version.string);
			jarFile = urllib.URLopener()
			versionFile = urllib.URLopener();
			if link['class'][0] == "client":
				savePath = "Minecraft/versions/"+fixedDate+"_"+releaseName+"_"+version.string+"_"+link['class'][0]
				if os.path.exists(savePath):
					if not os.path.isfile(savePath+"/" +fixedDate+"_"+releaseName+"_"+version.string+"_"+link['class'][0] +".jar"):
						jarFile.retrieve(link['href'], savePath+"/" +fixedDate+"_"+releaseName+"_"+version.string+"_"+link['class'][0] +".jar")
						print "Downloading client jar version " + version.string
					if not os.path.isfile(savePath+"/" +fixedDate+"_"+releaseName+"_"+version.string+"_"+link['class'][0] +".json"):
						jarFile.retrieve(link['href'], savePath+"/" +fixedDate+"_"+releaseName+"_"+version.string+"_"+link['class'][0] +".json")
						print "Downloading client version file " + version.string
				if not os.path.exists(savePath):
					os.mkdir(savePath)
					print "Created '"+savePath+"' directory"
					jarFile.retrieve(link['href'], savePath+"/" +fixedDate+"_"+releaseName+"_"+version.string+"_"+link['class'][0] +".jar")
					jarFile.retrieve(versionLink, savePath+"/" +fixedDate+"_"+releaseName+"_"+version.string+"_"+link['class'][0] +".json")
					print version.string
					print fixedDate
					print releaseName
					print link['class'][0]
					print link['href']
					print versionLink
					print "\n"
			if link['class'][0] == "server":
				savePath = "Minecraft/servers"
				if not os.path.isfile(savePath+"/" +fixedDate+"_"+releaseName+"_"+version.string+"_"+link['class'][0] +".jar"):
					jarFile.retrieve(link['href'], savePath+"/" +fixedDate+"_"+releaseName+"_"+version.string+"_"+link['class'][0] +".jar")
					print version.string
					print fixedDate
					print releaseName
					print link['class'][0]
					print link['href']
					print "\n"

	print "\n\n"