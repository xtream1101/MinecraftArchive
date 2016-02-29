import urllib2
import urllib
import json
import os
url = "https://launchermeta.mojang.com/mc/game/version_manifest.json"
DOWNLOADURL_json = "https://s3.amazonaws.com/Minecraft.Download/versions/:VERSION:/:VERSION:.json"
DOWNLOADURL_jar = "https://s3.amazonaws.com/Minecraft.Download/versions/:VERSION:/:VERSION:.jar"
DOWNLOADURL_serverjar = "https://s3.amazonaws.com/Minecraft.Download/versions/:VERSION:/minecraft_server.:VERSION:.jar"
request = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
page = urllib2.urlopen( request )

versionJSON = json.loads(page.read())['versions']

if not os.path.exists("Minecraft"):
	os.mkdir("Minecraft")
	print "Created Minecraft directory"
def createFolders(buildType):
	if not os.path.exists("Minecraft/"+buildType):
		os.mkdir("Minecraft/"+buildType)
	if not os.path.exists("Minecraft/"+buildType+"/versions"):
		os.mkdir("Minecraft/"+buildType+"/versions")
		print "Created "+buildType+" versions directory"
	if not os.path.exists("Minecraft/"+buildType+"/servers"):
		os.mkdir("Minecraft/"+buildType+"/servers")
		print "Created "+buildType+" servers directory"
createFolders("release") #stable
createFolders("snapshot") 
createFolders("old_beta")
createFolders("old_alpha")

for mcRelease in versionJSON:
	releaseName = mcRelease['type']
	releaseDate = mcRelease['releaseTime']
	fixedDate = releaseDate.split('-')
	fixedDate = fixedDate[0]+"."+fixedDate[1]+"."+fixedDate[2]
	fixedDate = fixedDate.split('T')[0]
	version = mcRelease['id']
	versionLink = DOWNLOADURL_json.replace(":VERSION:", version)
	jarLink = DOWNLOADURL_jar.replace(":VERSION:", version)
	serverjarLink = DOWNLOADURL_serverjar.replace(":VERSION:", version)
	
	
	

	jarFile = urllib.URLopener()
	savePath = "Minecraft/"+releaseName+"/versions/"+fixedDate+"_"+releaseName+"_"+version+"_"+"client"
	if os.path.exists(savePath):
		if not os.path.isfile(savePath+"/" +fixedDate+"_"+releaseName+"_"+version+"_"+"client" +".jar"):
			jarFile.retrieve(jarLink, savePath+"/" +fixedDate+"_"+releaseName+"_"+version+"_"+"client" +".jar")
			print "Downloading client jar version " + version
		if not os.path.isfile(savePath+"/" +fixedDate+"_"+releaseName+"_"+version+"_"+"client" +".json"):
			jarFile.retrieve(versionLink, savePath+"/" +fixedDate+"_"+releaseName+"_"+version+"_"+"client" +".json")
			print "Downloading client version file " + version
		if not os.path.isfile("Minecraft/"+releaseName+"/servers"+"/" +fixedDate+"_"+releaseName+"_"+version+"_"+"server" +".jar"):
			try:
				jarFile.retrieve(serverjarLink, "Minecraft/"+releaseName+"/servers"+"/" +fixedDate+"_"+releaseName+"_"+version+"_"+"server" +".jar")
				print "Downloading server file " + version
			except Exception:
				pass
	if not os.path.exists(savePath):
		os.mkdir(savePath)
		print "Created '"+savePath+"' directory"
		jarFile.retrieve(jarLink, savePath+"/" +fixedDate+"_"+releaseName+"_"+version+"_"+"client" +".jar")
		jarFile.retrieve(versionLink, savePath+"/" +fixedDate+"_"+releaseName+"_"+version+"_"+"client" +".json")
		try:
			jarFile.retrieve(serverjarLink, "Minecraft/"+releaseName+"/servers"+"/" +fixedDate+"_"+releaseName+"_"+version+"_"+"server" +".jar")
			dDownload = "yes"
		except Exception:
			dDownload = "no"
			print Exception
			pass
		print version
		print fixedDate
		print releaseName
		print "client"
		print jarLink
		print versionLink
		print "Downloaded server?: " + dDownload 
		print "\n"
