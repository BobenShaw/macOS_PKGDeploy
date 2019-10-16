# Bob's macOS Extract/Install Quick Script
# Written for applications like WebSense that run as PKGs but depend on files sitting with them.
# Optimized for Python 2.7+ because Apple never updated to modern/clean Python for some reason
# Hopefully your deployment software of choice will automatically escalate permissions!

# So we can download our payload
import urllib
# So we can extract the payload
import zipfile
# So we can reference macOS and ask it to politely install the PKG
import os

# Downloading our payload (Make sure this is accessible!)
urllib.urlretrieve ("http://thisisafake.server/EXAMPLEPACKAGE.zip", "EXAMPLEPACKAGE.zip")

# Extracting Payload from Package...
TestPayload = zipfile.ZipFile('EXAMPLEPACKAGE.zip')
TestPayload.extractall()
TestPayload.close()

# Time for the piece de resistance!
os.system("installer -pkg EXAMPLEPAYLOAD.pkg -target /")
