# Minecraft Archive


Downloads all versions of Minecraft (clients & servers), this includes builds from Alpha, Beta, Snapshot, and all stable releases.


## Requirements
* Python 2.7+
* Python library BeautifulSoup

## Use
Run `python minecraftArchive.py` and it will download all releases to a "Minecraft" folder from where you run the script.
The files will be organized in folders based on build type. Server files are currently unavailable for download for
alpha and beta versions of Minecraft.

An alternative to `minecraftArchive.py` is `minecraftArchive.noBS.py` this script does not require `beautifulsoup4` but still requires python 2.7+
which uses a Mojang hosted json file to generate download URL's
